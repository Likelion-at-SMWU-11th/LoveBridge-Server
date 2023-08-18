import os
from django.db import models
from accounts.models import *


class MyDocument(models.Model):
    file1 = models.CharField(verbose_name='가족관계증명서', max_length=300)
    file2 = models.CharField(verbose_name='주민등록등본', max_length=300)
    file3 = models.CharField(verbose_name='장애인등록증', max_length=300)
    file4 = models.CharField(verbose_name='정부기관심사결과지', max_length=300)

    def __str__(self):
        return str(self.file1)