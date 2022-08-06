# Generated by Django 3.2.15 on 2022-08-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageuni', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement', models.CharField(max_length=200)),
                ('course_name', models.CharField(max_length=200)),
                ('group_num', models.IntegerField()),
                ('course_num', models.IntegerField()),
                ('teacher', models.CharField(max_length=200)),
                ('start_time', models.TimeField()),
                ('stop_time', models.TimeField()),
                ('first_day', models.CharField(choices=[('saturday', 'saturday'), ('sunday', 'sunday'), ('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday')], max_length=200)),
                ('second_day', models.CharField(choices=[('saturday', 'saturday'), ('sunday', 'sunday'), ('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday')], max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='lifes',
            field=models.TextField(),
        ),
    ]
