#!/usr/bin/python3
# script to deploy an archive to web servers
import os
from fabric.api import *
import tarfile


@hosts(['104.196.19.203', '104.196.170.235'])
def do_deploy(archive_path):

    env.user = 'ubuntu'
    env.key_filename = '~/.ssh/id_rsa'

    try:
        if os.path.exists(archive_path):
            rfn = archive_path[9:-4]
            tarn = archive_path[9:]
            folder = "mkdir -p /data/web_static/releases/{}".format(rfn)
            foldername = "/data/web_static/releases/{}".format(rfn)
            run(folder)
            put(archive_path, '/tmp/')
            untar = "tar -C {} \
            -xzf /tmp/{}".format(foldername, tarn)
            run(untar)
            run("rm /tmp/{}".format(tarn))
            run("mv {}/web_static/* {}".format(foldername, foldername))
            run("rm -rf {}/web_static".format(foldername))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current")
            print("New version deployed!")
        else:
            print("no encontro")
            return False
    except Exception as e:
        print(e)
