from django.urls import path
from .views import contactus, signup, login_view, logout_user, profile_info, update_profile, manage,valid_courses

app_name = "account"
urlpatterns = [
    path('signup',signup, name="signup"),
    path('login',login_view, name="login"),
    path('logout',logout_user, name="logout"),
    path('contactus',contactus, name="contactus"),
    path('profile',profile_info, name="profile"),
    path('profile/update',update_profile, name="updateprofile"),
    path('manage',manage, name="manage"),
    path('manage/courses',valid_courses, name="validcourse"),
]