from django.db import models
from django.contrib.auth.models import User
from accounts.models import *


class Program(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True, default='')
    title = models.CharField(verbose_name='프로그램명', max_length=20)
    district = models.CharField(verbose_name="지역", max_length=11)
    agency = models.CharField(verbose_name="기관", max_length=15)
    deadline_yy = models.IntegerField(verbose_name="마감일 연")
    deadline_mm = models.CharField(verbose_name="마감일 월", max_length=2)
    deadline_dd = models.CharField(verbose_name="마감일 일", max_length=2)
    phone = models.CharField(verbose_name="문의처", max_length=13)
    like = models.IntegerField(verbose_name="좋아요 개수", default=0)
    iflike = models.BooleanField(verbose_name="좋아요 여부", default=False)
    category1 = models.CharField(verbose_name='카테고리1', max_length=20)
    category2 = models.CharField(verbose_name="카테고리2", max_length=20)
    applicant = models.IntegerField(verbose_name='신청 가능 인원', default=15)

    def __str__(self):
        return str(self.title)