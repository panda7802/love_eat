#!/usr/bin/env python
# coding=utf8
import os
import sys
import logging
from sys import platform, argv
from tutils.t_global_data import TGlobalData
from tutils import tconf
from tutils.t_log import TLog
from django.conf.locale import el
from tutils.t_yzm import clear_overtime_code_func

if __name__ == "__main__":
    print "Start ---------------------"
     
    if len(argv) > 1 and argv[1] == 'runserver' :
        TLog.init()
        TGlobalData.init()
        print "---------------------"
    # 测试还是正式程序
    if "win" in platform :
        tconf.PRO_TYPE = tconf.PRO_TYPE_DEV
    else :
        tconf.PRO_TYPE = tconf.PRO_TYPE_PRD
    # clear_overtime_code_func()
     
    print "type : " + tconf.PRO_TYPE
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "love_eat.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError , e:
            logging.exception(e)
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
