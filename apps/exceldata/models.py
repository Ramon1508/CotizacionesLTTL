from django.db import models


class ExcelData(models.Model):
    class Meta:
        verbose_name = 'ExcelData'
        verbose_name_plural = 'ExcelDatas'
    DataText = models.TextField()
