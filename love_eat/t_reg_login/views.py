# coding=utf-8

from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from t_reg_login.logic import t_family_reg
import logging
from tutils.tconf import T_SUCCESS
from django.views.decorators.csrf import csrf_exempt


def t_reg_view(req):
    res = render_to_response('reg.html')
    return res


def t_login_view(req):
    res = render_to_response('login.html')
    return res


def t_index_view(req):
    res = render_to_response('index.html')
    return res


def gen_yzm(req):
    res = t_family_reg.logic_gen_yzm(req)
    return res


def t_famliy_reg(req):
    res = t_family_reg.logic_famili_reg(req)
    logging.debug(res)
    return res


