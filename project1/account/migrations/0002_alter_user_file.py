# Generated by Django 3.2.14 on 2022-08-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='file',
            field=models.ImageField(upload_to='', verbose_name='بارگذاری فایل '),
        ),
    ]
