from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('profile_edit', views.customer_profile, name='profile_edit'),
    path('logout', views.logout_user, name='logout'),
]
