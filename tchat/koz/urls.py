from django.urls import path
from .import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.loginUser, name="login"),
    path('register', views.register, name="register"),
    path('post_message', views.sendmessage, name="post_message"),
]