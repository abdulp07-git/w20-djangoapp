from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('add/', views.add, name="add"),
    path('result/', views.result, name="result"),
    path('car/', views.car, name="car"),
    path('model/', views.model, name='model'),
    path('price/', views.price, name='price'),


]
