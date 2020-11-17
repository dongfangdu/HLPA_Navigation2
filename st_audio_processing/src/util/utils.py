# -*- coding: utf-8 -*-

"""
__author__ = Wangyd
__copyright__ = Copyright 2020
__version__ = 0.1
__status = Dev
"""

import os
import uuid


def get_uuid():
    return uuid.uuid4()


def get_project_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))


def get_images_dir():
    return os.path.abspath(os.path.join(get_project_dir(), "images"))


def get_audios_dir():
    return os.path.abspath(os.path.join(get_project_dir(), "audios"))


def get_enh_dir():
    return os.path.abspath(os.path.join(get_audios_dir(), "enh"))


def get_vc_dir():
    return os.path.abspath(os.path.join(get_audios_dir(), "vc"))


def get_tts_dir():
    return os.path.abspath(os.path.join(get_audios_dir(), "tts"))


def get_doc_dir():
    return os.path.abspath(os.path.join(get_project_dir(), "docs"))
