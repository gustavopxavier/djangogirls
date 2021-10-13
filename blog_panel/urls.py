from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel, name='PaginaInicial'),
    # path('', views.panel_navbar, name='panel_navbar'),
    # path('blogdashboard', views.blog_dashboard, name='blog_dashboard'),
]