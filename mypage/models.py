from django.db import models

class MyDocument(models.Model):
    file1 = models.FileField(verbose_name='가족관계증명서', null=True, upload_to="", blank=True)
    file2 = models.FileField(verbose_name='주민등록등본', null=True, upload_to="", blank=True)
    file3 = models.FileField(verbose_name='장애인등록증', null=True, upload_to="", blank=True)
    file4 = models.FileField(verbose_name='정부기관심사결과지', null=True, upload_to="", blank=True)