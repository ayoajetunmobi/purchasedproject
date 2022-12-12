from django.urls import path
from . import views
from .views import PassWordVerificationView

urlpatterns = [
  path('', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('reset/',views.password_reset, name= 'reset'),
   path('activated/<uidb64>/<token>/', PassWordVerificationView.as_view(), name='activated')
]