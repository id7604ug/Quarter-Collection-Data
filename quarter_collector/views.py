from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url
from .models import Quarter


# def quarter_list
def index(request):
    return render(request, 'index.html', {})


# def quarter_detail
def quarter_detail(request):
    return render(request, 'test.html')
