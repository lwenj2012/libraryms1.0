# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html')


def login_view(request):
    return render(request,'login.html')


def manager_view(request):
    return render(request,'manager.html')





def change_view(request):
    return render(request,'pwd_Modify.html')


def reader_view(request):
    return render(request,'reader.html')


def library_view(request):
    return render(request,'library_modify.html')


def readerType_view(request):
    return render(request,'readerType.html')


def parameter_view(request):
    return render(request,'parameter_modify.html')


def bremind_view(request):
    return render(request,'bremind.html')


def borrowQuery_view(request):
    return render(request,'borrowQuery.html')


def bookType_view(request):
    return render(request,'bookType.html')


def bookRenew_view(request):
    return render(request,'bookRenew.html')


def bookQuery_view(request):
    return render(request,'bookQuery.html')


def bookcase_view(request):
    return render(request,'bookcase.html')


def bookBorrow_view(request):
    return render(request,'bookBorrow.html')


def bookBack_view(request):
    return render(request,'bookBack.html')


def book_view(request):
    return render(request,'book.html')