# coding=utf-8

from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
import logging
import t_reg_logic
from django.views.decorators.csrf import csrf_exempt

from tutils.tjson import TJsonTools


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
    res = t_reg_logic.logic_gen_yzm(req)
    return res


@csrf_exempt
def t_family_reg_func(req):
    tmp_res = t_reg_logic.logic_family_reg(req)
    tmp_res = TJsonTools.tJsonEncode(tmp_res)
    logging.debug("t_family_reg_func : " + tmp_res)
    res = HttpResponse(tmp_res)
    return res

@csrf_exempt
def t_family_login_func(req):
    tmp_res = t_reg_logic.logic_family_login(req)
    tmp_res = TJsonTools.tJsonEncode(tmp_res)
    logging.debug("t_family_reg_func : " + tmp_res)
    res = HttpResponse(tmp_res)
    return res
