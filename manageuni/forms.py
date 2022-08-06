from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Course
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

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

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class CountactForm(forms.Form):
    title = forms.CharField(max_length=20)
    user_email = forms.EmailField(max_length=63)
    user_text = forms.CharField(max_length=250, min_length=10)

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    bio = forms.CharField(max_length=200, required=False)
    file = forms.ImageField(required=False)
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'bio', 'gender', 'lifes', 'file']

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