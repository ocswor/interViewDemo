from django.test import TestCase, Client
from user.models import User
import time
from hashlib import md5
import random


def generate_token():
    _token = "%s" % (time.time())
    _token = md5(_token.encode('utf-8')).hexdigest()
    return _token


# Create your tests here.

def generate_test_user():
    user_list = []
    for i in range(10):
        token = generate_token()
        name = "{}".format(int(time.time()))
        user = User.objects.create(client_token=token, name=name, score=random.randint(0, 100))
        user_list.append(user)
    return user_list


class UserScoreTestCase(TestCase):
    def setUp(self):
        self.user_list = generate_test_user()
        self.user = self.user_list[0]
        self.unlogin_client = Client()
        self.login_client = Client(HTTP_AUTHORIZATION=self.user.client_token)

    def tearDown(self) -> None:
        pass

    def test_post_userscore(self):
        path = "/userscore/{}/".format(self.user.id)
        response = self.unlogin_client.post(path)
        data = response.json()
        self.assertEqual(data['code'], -5000)

        response = self.login_client.post(path, {"score": 10000000})
        logindata = response.json()
        self.assertEqual(logindata['code'], 1)
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.score, 10000000)

    def test_get_userscore(self):
        path = "/userscore/{}/".format(self.user.id)

        a = random.randint(0, 10)
        b = random.randint(0, 10)
        if a > b:
            start, end = b, a
        else:
            start, end = a, b
        response = self.unlogin_client.get(path, {"start": start, "end": end})
        data = response.json()
        self.assertEqual(data['code'], -5000)

        response = self.login_client.get(path, {"start": start, "end": end})
        data = response.json()
        # print(data)
        self.assertEqual(data['code'], 1)
        self.assertEqual(len(data['data']["user_list"]), end-start)
        self.assertEqual(data['data']["user_info"]["score"], self.user.score)
