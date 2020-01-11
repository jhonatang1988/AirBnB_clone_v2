#!/usr/bin/python3
"""Do deploy static"""
from fabric.api import *
import os.path
import re


env.hosts = ['35.229.86.70', '35.237.216.255']


def do_deploy(archive_path):
    """distributes an archive"""
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, "/tmp/")
        file_name = re.search('versions/(.*).tgz',
                             archive_path)
        run("mkdir -p /data/web_static/releases/{}/"
            .format(file_name.group(1)))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name.group(1), file_name.group(1)))
        run("rm /tmp/{}.tgz".format(file_name.group(1)))
        run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/"
            .format(file_name.group(1), file_name.group(1)))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(file_name.group(1)))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name.group(1)))
        return True
    except:
        return False
