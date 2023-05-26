from operator import mod
from django.db import models

# Create your models here.
class Topic(models.Model):
    """Topic of learn log"""
    #Model API参考Django Model Field Reference
    text = models.CharField(max_length=200) #告诉Django在数据库预留多少空间
    date = models.DateTimeField(auto_now_add=True) #使用当前时间
    #提供显示信息的方法
    def __str__(self):
        return self.text