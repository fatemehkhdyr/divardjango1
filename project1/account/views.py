from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, CountactForm, UpdateProfileForm, CourseCreateForm
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User
from .models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Course
from django.contrib.auth.decorators import user_passes_test


def login_view(request):
    err_msg = ''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('demo:home')
            else:
                err_msg='we dont have user with this password'
                return render(
            request, 'account/login.html', context={'form': form, 'err_msg': err_msg})
    else:
        form = LoginForm()
        return render(
            request, 'account/login.html', context={'form': form, 'err_msg': err_msg})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('demo:home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('first_name')
            raw_password = form.cleaned_data.get('password1')
            user_email = form.cleaned_data.get('email')
            user = User(username= username, email=user_email)
            user.set_password(raw_password)
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('demo:home')

        else:
            return render(request, 'account/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'account/signup.html', {'form': form})


def contactus(request):
    if request.method == 'POST':
        form = CountactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('title')
            message = form.cleaned_data.get('user_text') + 'from' + form.cleaned_data.get('user_email') 
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['f.khodayari1132@gmail.com',]
            send_mail( subject, message, email_from, recipient_list )
            return render(request, 'account/contactus.html', {'form': form, 'valid':True})

        else:
            return render(request, 'account/contactus.html', {'form': form, 'valid':False})
    else:
        form = CountactForm()
        return render(request, 'account/contactus.html', {'form': form, 'valid':False})
@login_required
def profile_info(request):
    return render(request, 'account/profile.html')

@login_required
def update_profile(request):
    user = User.objects.get(pk=request.user.id)
    # last_gender = user.gender
    # user.gender = last_gender
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            bio = form.cleaned_data.get('bio')
            life = form.cleaned_data.get('lifes')
            if len(first_name):
                user.first_name = first_name
            if len(last_name):
                user.last_name = last_name
            if len(bio):
                user.bio = bio
            user.lifes = life
            
            user.save()
            return redirect('account:profile')

        else:
            return render(request, 'account/updateprofile.html', {'form': form})
    else:
        form = UpdateProfileForm()
        return render(request, 'account/updateprofile.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def manage(request):
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:validcourse')

        else:
            return render(request, 'account/manage_work.html', {'form': form})
    else:
        form = CourseCreateForm()
        return render(request, 'account/manage_work.html', {'form': form})

def valid_courses(request):
    courses = Course.objects.all()
    return render(request, 'account/validcourse.html', context={'courses':courses})
