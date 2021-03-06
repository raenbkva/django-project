# Generated by Django 3.2.2 on 2021-05-06 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210507_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(verbose_name='Название новости')),
                ('description', models.TextField(verbose_name='Текст новости')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.AlterModelOptions(
            name='dishesphoto',
            options={'verbose_name': 'Фото блюда', 'verbose_name_plural': 'Фото блюд'},
        ),
        migrations.CreateModel(
            name='NewsPhotos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo_url', models.TextField(verbose_name='Ссылка на фотографию')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Фотография к новости',
                'verbose_name_plural': 'Фотографии к новостям',
            },
        ),
    ]
