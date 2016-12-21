# coding=utf-8

from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
def t_reg(req):
    print "aa"
    res = HttpResponse('<h1>注册</h1>')
    return res

# Create your views here.
def index(req):
    res = render_to_response('index.html')
    return res

