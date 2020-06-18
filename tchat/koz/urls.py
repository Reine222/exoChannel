from django.urls import path
from .import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.loginUser, name="login"),
    path('salon', views.salon, name="salon"),
    path('register', views.register, name="register"),
    path('post_salon', views.sendsalon, name="post_salon"),
    path('post_message', views.connect, name="post_message"),
]