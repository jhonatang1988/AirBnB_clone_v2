#!/usr/bin/python3
"""
script to deploy an archive to web servers
"""
import os
from fabric.api import *
import tarfile


@hosts(['104.196.19.203', '104.196.170.235'])
def do_deploy(archive_path):
    """ deploy a folder"""

    env.user = 'ubuntu'
    env.key_filename = '~/.ssh/id_rsa'

    try:
        if os.path.exists(archive_path):
            rfn = archive_path[9:-4]
            tarn = archive_path[9:]
            folder = "mkdir -p /data/web_static/releases/{}".format(rfn)
            foldername = "/data/web_static/releases/{}/".format(rfn)
            put(archive_path, '/tmp/')
            run(folder)
            untar = "tar -xzf /tmp/{} -C {}".format(tarn, foldername)
            run(untar)
            run("sudo rm /tmp/{}".format(tarn))
            run("sudo mv {}web_static/* {}".format(foldername, foldername))
            run("sudo rm -rf {}web_static".format(foldername))
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s {} /data/web_static/current".format(foldername))
            print("New version deployed!")
            return True
        else:
            return False
    except Exception as e:
        print(e)
