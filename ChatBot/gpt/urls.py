from django.contrib import admin
from django.urls import path,include
from .views import UserView

urlpatterns = [
    path('bot/',UserView.as_view(),name='userview'),
]