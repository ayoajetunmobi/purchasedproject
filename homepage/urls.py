from django.urls import path
from . import views
from .views import VerificationView 

urlpatterns = [
  path('', views.index, name='home'),
  path('addPost/', views.getting_post , name='addPost'),
  path('delete/', views.delete, name= 'delete'),
  path('profileupdate/<int:id>', views.Prof_Update , name = 'profileUpdate'),
  path('review/',views.review , name = 'review'),
  path('bags/',views.bagsPage,name='bagsPage'),
  path('sneakers/',views.sneakers,name='sneakers'),
  path('jewelries/',views.jewelries,name='jewelries'),
  path('gown/',views.gown,name='gown'),
  path('ladies/',views.ladies_outfit,name='ladies_outfit'),
  path('shoprandom/',views.shoprandom,name='shoprandom'),
  path('cookedfood/',views.cookedfood,name='cookedfood'),
  path('bedsheet/',views.bedsheet,name='bedsheet'),
  path('clothing/',views.clothing,name='clothing'),
  path('food/',views.food,name='food'),
  path('fragrance/',views.fragrance,name='fragrance'),
  path('gadgets/',views.gadgets,name='gadgets'),
  path('graphics/',views.graphics,name='graphics'),
  path('postutme/',views.postutme,name='postutme'),
  path('trousers/',views.trousers,name='trousers'),
  path('wig/',views.wig,name='wig'),
  path('activate/<uidb64>/<token>/', VerificationView.as_view(), name='activate'),
  path('search/',views.search,name= 'search'),
  path('productspec/<int:id>',views.Product_spec,name= 'productspec'),
  path('changedp/',views.changedp, name='changedp'),
  path('register/', views.register, name = 'register'),
  path('settingsapi/', views.settingsfunctionality, name = 'settings'),
]
