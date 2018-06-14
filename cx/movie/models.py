from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField('电影名',max_length=255)
    rating = models.FloatField('评分',default=0)
    poster_url_big = models.URLField('电影封面-大',default='')
    poster_url_me = models.URLField('电影封面-小', default='')
    directors = models.CharField('导演', max_length=255)
    casts = models.CharField('演员', max_length=255)
    genes = models.CharField('类型', max_length=255)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    is_top = models.BooleanField('是否评分最高', default=False)
    is_in_theater = models.BooleanField('正在上映', default=True)

    def __str__(self):
        return self.name

class Cover(models.Model):
    name = models.CharField('封面名', max_length=100, default='cover')
    cover_img = models.ImageField('封面图片', upload_to='cover/', default='cover/default.jpg')
    is_alive = models.BooleanField('正在使用', default=False)