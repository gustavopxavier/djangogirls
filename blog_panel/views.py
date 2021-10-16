from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def dashboard(request):
    return render(request, 'blog_panel/dashboard.html')

def navbar(request):
    return render(request, 'blog_panel/navbar.html')

def modelo(request):
    return render(request, 'blog_panel/modelo.html')

def sobre(request):
    return render(request, 'blog_panel/sobre.html')

# class navbar(TemplateView):
#     template_name = 'blog_panel/navbar.html'
# 