from django.db import models
from django.contrib.auth.models import User


class Program(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True, default='')
    title = models.CharField(verbose_name='프로그램명', max_length=20)
    district = models.CharField(verbose_name="지역", max_length=11)
    ministry = models.CharField(verbose_name="기관", max_length=15)
    deadline_yy = models.IntegerField(verbose_name="마감일")
    deadline_mm = models.IntegerField(verbose_name="마감일")
    deadline_dd = models.IntegerField(verbose_name="마감일")
    phone = models.CharField(verbose_name="문의처", max_length=13)
    like = models.IntegerField(verbose_name="좋아요개수", default=0)
    iflike = models.BooleanField(verbose_name="좋아요여부", default=False)
    
    def __str__(self) :
        return str(self.title)


class MyLike(models.Model) :
    image = models.ImageField(verbose_name="사진")
    title = models.CharField(verbose_name='프로그램명', max_length=10)
    district = models.TextField(verbose_name="지역")
    ministry = models.TextField(verbose_name="기관")
    deadline = models.IntegerField(verbose_name="마감일")
    phone = models.TextField(verbose_name="문의처", )
    like = models.IntegerField(verbose_name="좋아요개수", default=0)
    iflike = models.BooleanField(verbose_name="좋아요여부", default=False)

    def __str__(self) :
        return str(self.title)
