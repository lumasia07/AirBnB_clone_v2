#!/usr/bin/python3
"""Deploy an archive script to web servers"""

from fabric.api import env, run, put, local
from datetime import datetime
import os


env.hosts = ['35.174.185.199', '52.4.81.70']

def do_pack():
    """
    Compresses contents of the web_static folder into an archive
    Return:
        Path to archive on success, otherwise None
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    arch_path = "versions/web_static_{}.tgz".format(timestamp)

    final = local("tar -cvzf {} web_static".format(arch_path))

    if final.succeeded:
        print("web-static packed: {} -> {}Bytes"
              .format(arch_path, os.path.getsize(arch_path)))
        return arch_path
    else:
        return None


def do_deploy(archive_path):
    """
    Distros archives to web servers
    Return:
        True if successful, otherwise false
    """
    if not os.path.exists(archive_path):
        print("Error: Archive not found".format(archive_path))
        return False

    arch_name = os.path.basename(archive_path)
    tmp_arch_path = "/tmp/{}".format(arch_name)
    put(archive_path, tmp_arch_path)

    relase_folder = "/data/web_static/releases/{}".format(arch_name)
    run("mkdir -p {}".format(release_folder))

    run("tar -xzf {} -C {}".format(tmp_arch_path, release_folder))

    run("rm {}".format(tmp_arch_path))

    extracted = "{}/web_static".format(release_folder)
    run("mv {}/. {}".format(extracted, release_folder))
    run("rm -rf {}".format(extracted))

    curr = "/data/web_static/current"
    run("rm -rf {}".format(curr))
    run("ln -s {} {}".format(release_folder, curr))

    print("New version deployed!")
    return True

