#!/usr/bin/python3
# build a tgz for fabfile
import tarfile
import os
import time
from fabric.api import *


def do_pack():
    print("hola")
    timestr = time.strftime("%Y%m%d%H%M%S")
    tgzfilename = 'versions/web_static_{}.tgz'.format(timestr)
    if not os.path.exists('versions'):
        try:
            local('mkdir versions')
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    try:
        with tarfile.open(tgzfilename, "w:gz") as tgz:
            local(tgz.add('web_static',
                          arcname=os.path.basename('web_static')))
            return name
    except:
        return None
