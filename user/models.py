from django.db import models


# Create your models here.

class User(models.Model):
    score = models.IntegerField(default=0, verbose_name="分数")
    client_token = models.CharField(max_length=64, verbose_name="客户端号,标示", unique=True)
    name = models.CharField(max_length=64, verbose_name="客户端名字")

    def __str__(self):
        return '%s(%s)' % (self.name, self.id)

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
