from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
path('',views.home,name="home"),

path('test/',views.test,name="test"),
path('change_lang/', views.change_lang, name='change_lang'),

]