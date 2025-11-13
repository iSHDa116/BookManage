from django.db import models
from .consts import MAX_RATE

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

CATEGORY = (('business','ビジネス'),('novel','小説'),('comic','漫画'),('life','生活'),('other','その他'))

class Book(models.Model):
    title = models.CharField(max_length=100)
    writter = models.CharField(max_length=50) #著者情報
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY)

    #作成したオブジェクトの持つ情報を返り値として送ることができる
    def __str__(self):
        return self.title

class Review(models.Model):
    # 他のモデルからフェーたを参照するのに使う-> ForeignKey(参照先のモデル、　削除した時の処理方法(今回は、両方消す))
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title