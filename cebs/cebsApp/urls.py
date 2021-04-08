from django.urls import path
from . import views

urlpatterns=[
    path('main/',views.main,name='main'),
    path('home/',views.home,name='home'),
    path('login/',views.loginForm,name='loginForm'),
    path('signup/',views.signup,name='signup'),
    path('productd/',views.productdetails,name='productd'),
    path('orderh/',views.orderhistory,name='orderh'),
    path('profile/',views.profile,name='profile'),
    path('cart/',views.usercart,name='cart'),
    path('signup/login/',views.loginForm,name='loginForm'),
    path('login/home/',views.home,name='home'),
    path('signup/home/',views.home,name='home'),
    path('signup/login/home/',views.home,name='home'),
    path('logout/', views.logoutUser, name="logout"),
    path('logout/main/',views.main,name="main")
]
