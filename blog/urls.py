from django.urls import path
from . import views
urlpatterns = [
  path('', views.index, name='blog'),
   path('<int:id>', views.Post_Specific, name='PostDetails'),
]