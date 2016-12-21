#!/usr/bin/env python
# coding=utf8
import os
import sys
from tutils.t_global_data import TGlobalData
from sys import platform
from tutils import tconf
import logging
from tutils.t_log import TLog
from love_eat.settings import STATIC_PATH


if __name__ == "__main__":
    print "Start ---------------------"
    TLog.init()
    TGlobalData.init()
    print "---------------------"
    # 测试还是正式程序
    if "win" in platform :
        tconf.PRO_TYPE = tconf.PRO_TYPE_PRD
    print "---------------static" ,STATIC_PATH
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
    logging.debug("----start run server")
    execute_from_command_line(sys.argv)
