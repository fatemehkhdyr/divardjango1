from django.urls import path
from .views import home, signup, login_view, logout_user, contactus, profile_info, edit_profile, manage, valid_courses

app_name = "manageuni"
urlpatterns = [
    path('home',home, name="home"),
    path('signup',signup, name="signup"),
    path('login',login_view, name="login"),
    path('logout',logout_user, name="logout"),
    path('contactus',contactus, name="contactus"),
    path('profile',profile_info, name="profile"),
    path('editprofile',edit_profile, name="edit"),
    path('manage',manage, name="manage"),
    path('manage/courses',valid_courses, name="validcourse"),
]