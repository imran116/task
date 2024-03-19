from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.index_view, name='home'),
    path('sign-up/', views.register_view, name='sign-up'),
    path('search/', views.get_recipe, name='search'),
    path('logout/', views.user_logout, name='logout'),


]