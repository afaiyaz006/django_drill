from dis import dis
from django.urls import path,include
from .views import indexView,signupView,afterloginView,logoutView

urlpatterns = [
   
    path('',indexView,name='index'),
    path('signup/',signupView,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('after_login/',afterloginView,name='after_login'),
    path('make_logout/',logoutView,name='make_logout')
]
