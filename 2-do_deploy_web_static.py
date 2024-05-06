#!/usr/bin/python3
"""Deploy an archive script to web servers"""

from fabric.api import env, run, put
import os


env.hosts = ['35.174.185.199', '52.4.81.70']

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

