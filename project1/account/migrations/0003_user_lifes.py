# Generated by Django 3.2.14 on 2022-08-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lifes',
            field=models.TextField(default='salam'),
        ),
    ]
