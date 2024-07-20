from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_person/', views.add_person, name='add_person'),
    path('', views.home, name='home'),
]
