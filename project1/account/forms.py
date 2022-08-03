from dataclasses import fields
from pickle import FALSE
from pyexpat import model
from random import choices
from django import forms
from django.core.exceptions import ValidationError
from .models import User
from .models import Course


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class CountactForm(forms.Form):
    title = forms.CharField(max_length=20)
    user_email = forms.EmailField(max_length=63)
    user_text = forms.CharField(max_length=250, min_length=10)


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        username = cleaned_data.get("first_name")

        if password1!=password2:
            raise ValidationError(
                " password and password repeat is not same"
            )
        if User.objects.filter(username = username).count()!=0:
            raise ValidationError(
                " username is duplicate"
            )

class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'bio','gender','file', 'lifes']

class CourseCreateForm(forms.ModelForm):
    DAY_CHOICES = (
    ("saturday", "saturday"),
    ("sunday", "sunday"),
    ("monday", "monday"),
    ("tuesday", "tuesday"),
    ("wednesday", "wednesday")
)
    start_time = forms.TimeField(input_formats= ('%H:%M',) )
    stop_time = forms.TimeField(input_formats= ('%H:%M',) )
    second_day = forms.ChoiceField(required=False, choices = DAY_CHOICES)
    class Meta:
        model = Course
        fields = ['departement', 'course_name','group_num', 'course_num', 'teacher', 'start_time', 'stop_time', 'first_day', 'second_day']