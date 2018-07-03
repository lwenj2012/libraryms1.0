# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
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
    if request.method == 'GET':
        lib_list = LibraryInfo.objects.all()
        return render(request, 'library_modify.html',{'lib_list':lib_list})
    if request.method == 'POST':
        lib_name = request.POST.get('libraryname','')
        lib_manager = request.POST.get('curator','')
        lib_phone = request.POST.get('tel','')
        lib_location = request.POST.get('address','')
        lib_email = request.POST.get('email','')
        lib_url = request.POST.get('url','')
        lib_build = request.POST.get('createDate','')
        lib_info = request.POST.get('introduce','')
        if not LibraryInfo.objects.all():
            LibraryInfo.objects.create(lib_name=lib_name,lib_manager=lib_manager,lib_phone=lib_phone,lib_location=lib_location,lib_email=lib_email,lib_url=lib_url,lib_build=lib_build,lib_info=lib_info)
        else:
            LibraryInfo.objects.filter(lib_id=1).update(lib_name=lib_name,lib_manager=lib_manager,lib_phone=lib_phone,lib_location=lib_location,lib_email=lib_email,lib_url=lib_url,lib_build=lib_build,lib_info=lib_info)
        lib_list = LibraryInfo.objects.all()
        return render(request,'library_modify.html',{'lib_list':lib_list})


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