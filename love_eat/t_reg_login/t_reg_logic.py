# coding=utf-8

'''
Created on 2016年12月22日

@author: pangt
'''
from urllib import urlencode, quote

from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from tutils.t_response import TResponse
from tutils.tconf import T_SUCCESS
import logging
from tutils import t_yzm, t_encrypt_decrypt
from tutils.tjson import TJsonTools
from tutils.t_encrypt_decrypt import TEncryptDecrypt
from models import Family


def logic_gen_yzm(req):
    yzm_res = t_yzm.gene_code()
    if T_SUCCESS == yzm_res.res:
        yzm_res.text = TEncryptDecrypt.md5_str(yzm_res.text)[0:8]
        logging.info("gen : " + TEncryptDecrypt.md5_str(yzm_res.text))

    res_json = TJsonTools.tJsonEncode(yzm_res)
    res = HttpResponse(res_json)
    return res

@csrf_exempt
def logic_family_reg(req):
    family_name = ""
    passwd = ""
    res = TResponse()
    if req.method == 'POST':
        family_name = req.POST.get('familyName', "")
        passwd = req.POST.get('passwd', "")
    elif req.method == 'GET':
        family_name = req.GET.get('familyName', "")
        passwd = req.GET.get('passwd', "")
    else:
        res.res = False
        res.msg = "请求方式有误"
        return

    logging.info("logic_family_reg : " + passwd + " , " + family_name)

    db_family = Family()

    if 0 == len(family_name) * len(passwd):
        res.res = False
        res.msg = "长度不可为0"
        return res
    try:
        # 判断是否重复
        tmp = Family.objects.filter(name=family_name)
        if len(tmp) > 0:
            res.res = False
            res.msg = "用户名已存在"
            return res
        db_family.passwd = passwd
        db_family.name = family_name
        db_family.save()
    except Exception, e:
        logging.exception(e)
        res.res = False
        res.msg = "提交异常，请重试"
        return res

    # 记录到数据库
    res.res = True
    res.msg = ""
    res.action = "index.html"
    return res

@csrf_exempt
def logic_family_login(req):
    family_name = ""
    passwd = ""
    res = TResponse()
    if req.method == 'POST':
        family_name = req.POST.get('familyName', "")
        passwd = req.POST.get('passwd', "")
    elif req.method == 'GET':
        family_name = req.GET.get('familyName', "")
        passwd = req.GET.get('passwd', "")
    else:
        res.res = False
        res.msg = "请求方式有误"
        return

    logging.info("logic_family_login : " + passwd + " , " + family_name)

    db_family = Family()

    if 0 == len(family_name) * len(passwd):
        res.res = False
        res.msg = "长度不可为0"
        return res
    try:
        # 判断是否重复
        tmp = Family.objects.filter(name=family_name)
        if len(tmp) <= 0:
            res.res = False
            res.msg = "用户名不存在"
            return res
        tmp = tmp[0];
        right_passwd = tmp.passwd
        if right_passwd != passwd :
            res.res = False
            res.msg = "密码错误"
            return res
    except Exception, e:
        logging.exception(e)
        res.res = False
        res.msg = "提交异常，请重试"
        return res

    # 记录到数据库
    res.res = True
    res.msg = ""
    res.action = "index.html"
    return res

