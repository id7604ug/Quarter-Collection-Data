from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url
from .forms import QuarterForm
from .models import Quarter


# def quarter_list
def index(request):
    quarter_list = Quarter.objects.all()
    return render(request, 'index.html', {"quarters":quarter_list})


# def quarter_detail
def quarter_detail(request):
    quarters = Quarter.objects.all()

    form = QuarterForm()
    data = {'quarters':quarters, 'form':form}
    return render(request, 'quarter_detail.html', data)


def edit_quarter(request):
    return render(request, 'test.html', {})
