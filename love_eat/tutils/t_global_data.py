# coding=utf8

'''
Created on 20161215

@author: pangt
'''

import logging
from os.path import os
from sys import platform

from tutils.t_log import TLog
from love_eat import settings


class TGlobalData :
    
    plam = "unix"
    FILE_PATH = settings.BASE_DIR + "/files/"
    
    @staticmethod
    def init():
        '''
        初始化
        '''
        logging.info("-------Global_data init")
        TGlobalData.plam = platform
        logging.info("-------FILE_PATH " + TGlobalData.FILE_PATH)
        logging.info("-------Global_data init over")
    
    @staticmethod
    def is_test_pro():
        '''
        是否为测试程序
        '''
        res = (TGlobalData.PRO_TYPE == TGlobalData.PRO_TYPE_DEV)
        return res
