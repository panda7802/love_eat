# coding=utf8

'''
Created on 2016å¹?12æœ?5æ—?

@author: pangt
'''

from os.path import os
from sys import platform

from django.conf import settings


class TGlobalData :
    
    plam = "unix"
    FILE_PATH = settings.BASE_DIR + "/files/"
    
    @staticmethod
    def init():
        print "-------Global_data init" 
        TGlobalData.plam = platform
        print "-------FILE_PATH" , TGlobalData.FILE_PATH
        print "-------Global_data init over"
       
# tGlobalData = TGlobalData() 
