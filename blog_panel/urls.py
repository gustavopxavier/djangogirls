from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('navbar', views.navbar, name='navbar'),
    path('sobre', views.sobre, name='sobre'),
    path('dashboard', views.dashboard, name='dashboard'),
    # path('modelo', views.modelo, name='modelo'),
    # path('blogdashboard', views.blog_dashboard, name='blog_dashboard'),
]