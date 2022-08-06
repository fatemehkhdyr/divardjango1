from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
    ("man", "man"),
    ("woman", "woman"))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    bio = models.CharField(max_length=200)
    file = models.ImageField(verbose_name="بارگذاری فایل ")
    lifes = models.TextField()


class Course(models.Model):
    DAY_CHOICES = (
    ("saturday", "saturday"),
    ("sunday", "sunday"),
    ("monday", "monday"),
    ("tuesday", "tuesday"),
    ("wednesday", "wednesday")
)
    departement = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    group_num = models.IntegerField()
    course_num = models.IntegerField()
    teacher = models.CharField(max_length=200)
    start_time = models.TimeField()
    stop_time = models.TimeField()
    first_day = models.CharField(max_length = 200, choices=DAY_CHOICES)
    second_day = models.CharField(max_length = 200, null=True, choices=DAY_CHOICES)

    def __str__(self) -> str:
        return 'generate {} in {} department'.format(self.course_name, self.departement)