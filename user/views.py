from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from common.custom_decorators import login_required
from user.models import User


@method_decorator(login_required, name='dispatch')
class UserScore(View):
    def post(self, request):
        try:
            score = request.POST.get("score")
            user = request.user
            user.score = score
            user.save()
        except Exception as e:
            return JsonResponse({'code': -1, 'msg': '参数错误'})
        return JsonResponse(data={
            "code": 1,
            'msg': 'success'
        })


@method_decorator(login_required, name='dispatch')
class ScoreRank(View):
    def get(self, request):
        start = int(request.GET.get("start", 0))
        end = int(request.GET.get("end", 0))
        key_user = request.user
        user_list = User.objects.values("score", "name").order_by("-score")[start:end]
        data = {
            "user_list": list(user_list),
            "user_info": {
                "name": key_user.name,
                "score": key_user.score
            }
        }
        return JsonResponse(data={
            "code": 1,
            "data": data
        })
