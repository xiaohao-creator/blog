# Generated by Django 2.2 on 2020-07-31 05:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20200731_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='displaytype',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
    ]
