# views.py

from django.shortcuts import render

def VueView(request):
    return render(request, 'index.html')
