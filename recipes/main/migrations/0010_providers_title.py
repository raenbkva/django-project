# Generated by Django 3.2.2 on 2021-05-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_providers_since'),
    ]

    operations = [
        migrations.AddField(
            model_name='providers',
            name='title',
            field=models.TextField(default=1, verbose_name='Название поставщика'),
            preserve_default=False,
        ),
    ]