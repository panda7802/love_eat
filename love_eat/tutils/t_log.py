# coding=utf-8

'''
Created on 2016�?12�?9�?

@author: pangt
'''

import logging
from logging.handlers import RotatingFileHandler
import traceback


class TLog :
    
    def init(self):
        LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        print "start init log"
        #logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt='%Y-%m-%d %H:%M.%S',
                    )   
          
        # 定义�?个RotatingFileHandler，最多备�?5个日志文件，每个日志文件�?�?10M
        rthandler = RotatingFileHandler('myapp.log', maxBytes=10 * 1024 * 1024, backupCount=5)
        rthandler.setLevel(logging.INFO)
        formatter = logging.Formatter(LOG_FORMAT)
        rthandler.setFormatter(formatter)
        logging.getLogger('').addHandler(rthandler)
    
    def debug(self,msg):
        logging.debug(msg)
    
    def info(self,msg):
        logging.info(msg)
    
    def error(self,msg):
        logging.error(msg)
    
    def exception(self,e):
        logging.exception(e)

tlog=TLog();

if "__main__" == __name__ :
    tlog.init()
    try :
        tlog.debug("panda debug")
        tlog.info("info")
        tlog.error("err panda")
        i = 6 / 0
    except Exception , e:
        print e
#         traceback.print_stack()
        tlog.exception(e)
