# Generated by Django 2.0 on 2018-06-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='cover', max_length=100, verbose_name='封面名')),
                ('cover_img', models.ImageField(default='cover/default.jpg', upload_to='cover/', verbose_name='封面图片')),
                ('is_alive', models.BooleanField(default=False, verbose_name='正在使用')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='电影名')),
                ('rating', models.FloatField(default=0, verbose_name='评分')),
                ('postr_url_big', models.URLField(default='', verbose_name='电影封面-大')),
                ('postr_url_me', models.URLField(default='', verbose_name='电影封面-小')),
                ('directors', models.CharField(max_length=255, verbose_name='导演')),
                ('casts', models.CharField(max_length=255, verbose_name='演员')),
                ('genes', models.CharField(max_length=255, verbose_name='类型')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_top', models.BooleanField(default=False, verbose_name='是否评分最高')),
                ('is_in_theater', models.BooleanField(default=True, verbose_name='正在上映')),
            ],
        ),
    ]
