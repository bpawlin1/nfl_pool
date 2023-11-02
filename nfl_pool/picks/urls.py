# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make_pick/', views.make_pick, name='make_pick'),
    path('register/', views.register, name='register'),
]