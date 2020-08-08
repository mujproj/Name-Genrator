from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index1, name='index1'),
    path('/index2', views.index2, name='index2'),
]
