from django.shortcuts import render

# Create your views here.
def panel(request):
    return render(request, 'blog_panel/panel.html')
