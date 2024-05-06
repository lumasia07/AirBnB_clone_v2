#!/usr/bin/python3
"""Archives contents of web_static into a tgz"""

from fabric.api import local
from datetime import datetime
import os


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
