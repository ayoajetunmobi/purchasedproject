from django.urls import path
from . import views


urlpatterns = [ path('', views.home, name='notification'),
               path('send_push/', views.send_push)
               ] 
