# -*- coding:utf-8 -*-
import os
import sys
import uuid
from configparser import ConfigParser
import time


class ConfigDictParser(ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k, v in d.items():
            d[k] = dict(v)
        return d


def get_project_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))


def get_src_dir():
    return os.path.join(get_project_dir(), 'src')


def get_app_dir():
    return os.path.join(get_src_dir(), 'app')


def get_config_dict(conf_file='config.ini', conf_path='./cfg'):
    if conf_path[0] != '/':
        conf_path = os.path.abspath(os.path.join(get_project_dir(), conf_path))
    conf_file = os.path.join(conf_path, conf_file)
    # print(conf_file)
    if not os.path.exists(conf_file):
        raise RuntimeError(u'配置文件不存在')

    cf = ConfigDictParser()
    cf.read(conf_file)
    # pprint(cf.as_dict())

    return cf.as_dict()


def get_package_path():
    dirname_list = [dirname for dirname in sys.path if 'site-packages' in dirname]
    return os.path.abspath(dirname_list[0]) if len(dirname_list) > 0 else None


def get_abs_path(inp_path):
    if inp_path[0] != '/':
        out_path = os.path.abspath(os.path.join(get_project_dir(), inp_path))
    else:
        out_path = inp_path
    if not os.path.exists(out_path):
        raise RuntimeError(u'%s文件路径不正确' % out_path)
    return out_path


def get_uuid():
    guid = uuid.uuid4()
    return str(guid).replace('-', '')


def current_timestamp_sec():
    return int(time.time())


def get_config_py_path(conf_file="configure.py", conf_path="./cfg"):
    if conf_path[0] != '/':
        conf_path = os.path.abspath(os.path.join(get_project_dir(), conf_path))
    conf_file = os.path.join(conf_path, conf_file)
    # print conf_file
    if not os.path.exists(conf_file):
        raise RuntimeError(u'配置文件不存在')
    return conf_file

