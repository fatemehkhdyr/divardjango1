from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import User, Course
from .forms import SignUpForm, LoginForm, CountactForm, EditProfileForm, CourseCreateForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def home(request):
    return render(request, 'manageuni/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('manageuni:home')
    else:
        form = SignUpForm()
    return render(request, 'manageuni/signup.html', {'form': form})

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
                return redirect('manageuni:home')
            else:
                err_msg='we dont have user with this password'
                return render(
            request, 'manageuni/login.html', context={'form': form, 'err_msg': err_msg})
    else:
        form = LoginForm()
        return render(
            request, 'manageuni/login.html', context={'form': form, 'err_msg': err_msg})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('manageuni:home')

def contactus(request):
    if request.method == 'POST':
        form = CountactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('title')
            message = form.cleaned_data.get('user_text') + 'from' + form.cleaned_data.get('user_email') 
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['f.khodayari1132@gmail.com',]
            send_mail( subject, message, email_from, recipient_list )
            return render(request, 'manageuni/contactus.html', {'form': form, 'valid':True})

        else:
            return render(request, 'manageuni/contactus.html', {'form': form, 'valid':False})
    else:
        form = CountactForm()
        return render(request, 'manageuni/contactus.html', {'form': form, 'valid':False})

@login_required
def profile_info(request):
    return render(request, 'manageuni/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, files=request.FILES, instance=User.objects.get(username=request.user.username))
        if form.is_valid():
            form.save()
            return redirect('manageuni:profile')

        else:
            return render(request, 'manageuni/updateprofile.html', {'form': form})
    else:
        form = EditProfileForm(instance=User.objects.get(username=request.user.username))
        return render(request, 'manageuni/updateprofile.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def manage(request):
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manageuni:validcourse')

        else:
            return render(request, 'manageuni/manage_work.html', {'form': form})
    else:
        form = CourseCreateForm()
        return render(request, 'manageuni/manage_work.html', {'form': form})

def valid_courses(request):
    courses = Course.objects.all()
    return render(request, 'manageuni/validcourse.html', context={'courses':courses})
