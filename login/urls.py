from django.urls import path
from . import views
from .views import VerificationView 

urlpatterns = [
  path('', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('reset/',views.password_reset, name= 'reset'),
   path('activate/<uidb64>/<token>/', VerificationView.as_view(), name='activate')
]