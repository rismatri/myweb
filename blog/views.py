# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from.models import Artikel

# Create your views here.
def index(request):
    return render(request, 'layout/index.html')
def about(request):
    return render(request, 'layout/about.html')
def contact(request):
    return render(request, 'layout/contact.html')
def blog(request):
    # select * from Artikel
    blogs = Artikel.objects.all()
    return render(request, 'layout/blog.html', {'blogs':blogs})
