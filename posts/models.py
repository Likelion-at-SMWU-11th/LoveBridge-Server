from django.db import models
from django.contrib.auth.models import User


class Program(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True, default='')
    title = models.CharField(verbose_name='프로그램명', max_length=20)
    district = models.CharField(verbose_name="지역", max_length=11)
    agency = models.CharField(verbose_name="기관", max_length=15)
    deadline_yy = models.IntegerField(verbose_name="마감일 연")
    deadline_mm = models.IntegerField(verbose_name="마감일 월")
    deadline_dd = models.IntegerField(verbose_name="마감일 일")
    phone = models.CharField(verbose_name="문의처", max_length=13)
    like = models.IntegerField(verbose_name="좋아요 개수", default=0)
    iflike = models.BooleanField(verbose_name="좋아요 여부", default=False)
    ifregister = models.BooleanField(verbose_name="신청 여부", default=False)
    category = models.ManyToManyField('Category', verbose_name="카테고리", blank=True)
    
    def __str__(self):
        return str(self.title)


class Category(models.Model):
    detail_category = models.CharField(max_length=50)

    def __str__(self):
        return self.detail_category
