# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from models import *
# Create your views here.
def index_view(request):
    uname = request.session['admin_name']
    return render(request, 'index.html', {'uname': uname})


def login_view(request):
    if request.method == 'GET':
        #cookies信息
        if request.COOKIES.has_key('loginUser'):
            loginUser = request.COOKIES.get('loginUser', '').split(',')
            name = loginUser[0]
            pwd = loginUser[1]

            return render(request, 'login.html', {'name': name, 'pwd': pwd})
        #如果请求方式是get就直接显示登录界面
        return render(request,'login.html')
    else:
        # 1.获取请求参数
        name = request.POST.get('name')
        PWD = request.POST.get('pwd')
        flag = request.POST.get('flag')
        response = HttpResponse()
        if Admin.objects.filter(admin_name=name,admin_password=PWD):
            request.session['admin_name'] = name
            response.status_code = 302
            response.setdefault('Location', '/')
            if flag == '1':
                response.set_cookie('loginUser', name + ',' + PWD, max_age=3 * 24 * 60 * 60, path='/login/')

                return response
            else:
                response.delete_cookie('loginUser', path='/login/')
                return response
        else:
            response.delete_cookie('loginUser', path='/login/')
            response.status_code = 302
            response.setdefault('Location', '/login/')
            return response


def manager_view(request):
    uname = request.session['admin_name']
    return render(request, 'manager.html', {'uname': uname})



def change_view(request):
    uname = request.session['admin_name']
    return render(request, 'pwd_Modify.html', {'uname': uname})


def reader_view(request):
    uname = request.session['admin_name']
    readerlist = Reader.objects.all()
    return render(request, 'reader.html', {'uname': uname, 'readerlist': readerlist})


def library_view(request):
    uname = request.session['admin_name']
    if request.method == 'GET':
        lib_list = LibraryInfo.objects.all()
        return render(request, 'library_modify.html',{'lib_list':lib_list,'uname': uname})
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
        return render(request,'library_modify.html',{'lib_list':lib_list,'uname': uname})


def readerType_view(request):
    uname = request.session['admin_name']
    readerTypelist = ReaderType.objects.all()
    return render(request, 'readerType.html', {'uname': uname, 'readerTypelist': readerTypelist})


def parameter_view(request):
    uname = request.session['admin_name']
    return render(request, 'parameter_modify.html', {'uname': uname})


def bremind_view(request):
    uname = request.session['admin_name']
    borrowlist = BookBorrow.objects.all()
    return render(request, 'bremind.html', {'uname': uname, 'borrowlist': borrowlist})


def borrowQuery_view(request):
    uname = request.session['admin_name']
    borrowlist = BookBorrow.objects.all()

    return render(request, 'borrowQuery.html', {'uname': uname, 'borrowlist': borrowlist})


def bookType_view(request):
    uname = request.session['admin_name']
    bookTypelist = BookType.objects.all()
    return render(request, 'bookType.html', {'uname': uname, 'bookTypelist': bookTypelist})


def bookRenew_view(request):
    uname = request.session['admin_name']
    return render(request, 'bookRenew.html', {'uname': uname})


def bookQuery_view(request):
    uname = request.session['admin_name']
    booklist = Book.objects.all()
    return render(request, 'bookQuery.html', {'uname': uname, 'booklist': booklist})


def bookcase_view(request):
    uname = request.session['admin_name']
    return render(request, 'bookcase.html', {'uname': uname})


def bookBorrow_view(request):
    uname = request.session[u'admin_name']
    return render(request, 'bookBorrow.html', {'uname': uname})


def bookBack_view(request):
    uname = request.session['admin_name']
    return render(request, 'bookBack.html', {'uname': uname})


def book_view(request):
    uname = request.session['admin_name']
    booklist = Book.objects.all()
    return render(request, 'book.html', {'uname': uname, 'booklist': booklist})