from django.db import models

# Create your models here.

# class SampleModel(models.Model):
#     title = models.CharField(max_length=100)
#     number = models.IntegerField()
#     date = models.DateField()

CATEGORY = (('business','ビジネス'),('novel','小説'),('life','生活'),('other','その他'))

class Book(models.Model):
    title = models.CharField(max_length=100)
    writter = models.CharField(max_length=50)
    text = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY)

    #作成したオブジェクトの持つ情報を返り値として送ることができる
    def __str__(self):
        return self.title