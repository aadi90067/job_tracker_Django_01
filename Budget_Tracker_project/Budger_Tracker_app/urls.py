from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Register',views.Register,name='Register'),
    path('user_login',views.user_login,name='user_login'),
    path('Dashboard',views.Dashboard,name='Dashboard'),
    path('clear/', views.clear_expenses, name='clear_expenses'),
    path('logout/', views.user_logout, name='user_logout'),


]