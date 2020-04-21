from django.http.response import JsonResponse
from user.models import User


def login_required(func):
    def _wrapper(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return JsonResponse({'code': -5000, 'msg': '非法用户'})
        try:
            user = User.objects.get(client_token=token)
            request.user = user
            return func(request, *args, **kwargs)
        except User.DoesNotExist as e:
            return JsonResponse({'code': -5000, 'msg': '非法用户'})
    return _wrapper
