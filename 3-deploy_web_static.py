#!/usr/bin/python3
"""Full deployment"""

from fabric.api import env, run, put, local, cd
from datetime import datetime
import os


env.hosts = ['35.174.185.199', '52.4.81.70']
env.user = "ubuntu"

def do_pack():
    """
    Returns arch path
    """
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(date)
        arch_file = local("tar -cvzf {} web_static".format(file_path))
        if arch_file.succeeded:
            return file_path
    except Execption as e:
        return None

def do_deploy(archive_path):
    """
    Distros archives to web servers
    Return:
        True if successful, otherwise false
    """
    if os.path.exists(archive_path):
        archived_file = os.path.basename(archive_path)
        newest_version = "/data/web_static/releases/{}".format(
            archived_file[:-4])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        with cd(newest_version):
            run("sudo tar -xzf /tmp/{} -C .".format(archived_file))
            run("sudo rm /tmp/{}".format(archived_file))
            run("sudo mv web_static/* .")
            run("sudo rm -rf web_static")
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False

def deploy():
    """Deploy the web_static content to web servers"""
    arch_path = do_pack()
    if not arch_path:
        return False

    return do_deploy(arch_path)
