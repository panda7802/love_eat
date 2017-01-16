# coding=utf-8

'''
Created on 2016年12月22日

@author: pangt
'''
from django.http.response import HttpResponse
from tutils.tconf import T_SUCCESS
import logging
from tutils import t_yzm, t_encrypt_decrypt
from tutils.tjson import TJsonTools
from tutils.t_encrypt_decrypt import TEncryptDecrypt


def logic_gen_yzm(req):
    yzm_res = t_yzm.gene_code()
    if T_SUCCESS == yzm_res.res:
        yzm_res.text = TEncryptDecrypt.md5_str(yzm_res.text)[0:8]
        logging.info("gen : " + TEncryptDecrypt.md5_str(yzm_res.text))

    res_json = TJsonTools.tJsonEncode(yzm_res)
    res = HttpResponse(res_json)
    return res


def logic_famili_reg(req):
    familyName = req.GET.get('familyName', "")
    passwd = req.GET.get('passwd', "")
    logging.info("logic_famili_reg : " + passwd + " , " + familyName)
    res = HttpResponse("a")
    return res
