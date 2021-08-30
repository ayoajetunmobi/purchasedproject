from django.urls import path
from . import views



urlpatterns = [
  path('', views.formsdispaly, name='home'),
  path('addPost/', views.getting_post , name='addPost'),
  path('delete/', views.delete, name= 'delete'),
  path('profileupdate/', views.Prof_Update , name = 'profileUpdate'),
  path('my_profile/', views.get_profile , name = 'myprofile'),
  path('list_display/',views.pagination_page,name='userList'),
  path('search/',views.search,name= 'search'),
  path('productspec/',views.Product_spec,name= 'productspec'),
  path('contacted/',views.whencontacted,name= 'contacted'),
  path('msg/',views.msgDisplay,name= 'getMsgs'),
  path('signals/',views.Signals,name= 'signals'),
  path('suggest/',views.suggestproduct, name='suggest'),
]