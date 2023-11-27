from django.urls import path
from . import views
app_name ='school_app'
urlpatterns =[
    path('',views.home,name='home'),
    path('new', views.new, name='new'),
    path('form',views.form,name='form'),
    path('message',views.message,name='message')
]