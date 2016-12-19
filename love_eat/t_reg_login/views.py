# coding=utf-8

from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def t_reg(req):
    print "aa"
    res = HttpResponse('<h1>注册</h1>')
    return res

