from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('', profile, name='profile'),
    path('add/',views.func, name='add'),
    # path('map/', map_view, name='map'),
     path('login/', views.login_user, name ='login'),
      path('register/', views.register_user, name='register'),
      
]
