from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('map/', profile, name='profile'),
    
    path('add/',views.func, name='add'),
     path('', views.login_user, name ='login'),
      path('register/', views.register_user, name='register'),
      
]
