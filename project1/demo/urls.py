from django.urls import path
from .views import home

app_name = "demo"
urlpatterns = [
    path('home',home, name="home"),
]