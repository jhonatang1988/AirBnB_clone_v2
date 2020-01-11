#!/usr/bin/python3
# build a tgz for fabfile
import tarfile
import os
import time
from fabric.api import *


def do_pack():

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

"""
script to deploy an archive to web servers
"""
import os
from fabric.api import *
import tarfile

env.hosts = ['35.227.82.74', '35.231.166.249']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ deploy a folder"""

    if not os.path.exists(archive_path):
        return (False)

    try:
        rfn = archive_path[9:-4]
        tarn = archive_path[9:]
        folder = "mkdir -p /data/web_static/releases/{}/".format(rfn)
        foldername = "/data/web_static/releases/{}/".format(rfn)
        put(archive_path, "/tmp/")
        run(folder)
        untar = "tar -xzf /tmp/{} -C {}".format(tarn, foldername)
        run(untar)
        run("rm /tmp/{}".format(tarn))
        run("mv {}web_static/* {}".format(foldername, foldername))
        run("rm -rf {}web_static".format(foldername))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(foldername))
        print("New version deployed!")
        return True
    except Exception as e:
        print(e)

def deploy():
    if not os.path.exists(archive_path):
        return False
    apath = do_pack()
    res = do_deploy(apath)
    return res
