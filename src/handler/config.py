# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/10/13.
  获取本地目录, 如果有配置文件，沿用之
"""
from ..g import pro_env
from os import path, makedirs
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class BaseConfig:
    def __init__(self):
        self.data_dir = path.join(pro_env.program_base, 'data')


class ConfigHandler:
    @classmethod
    def init(cls):
        cfg_path = path.join(pro_env.program_base, 'config.yaml')

        if not path.exists(cfg_path):
            base_cfg = BaseConfig()
            makedirs(base_cfg.data_dir, exist_ok=True)

            with open(cfg_path, 'w', encoding='utf-8') as cfg_file:
                dump(base_cfg.__dict__, cfg_file, Dumper=Dumper)

            pro_env.data_dir = base_cfg.data_dir
        else:
            # 读取
            cfg = load(open(cfg_path, 'r', encoding='utf-8'), Loader=Loader)

            if 'data_dir' not in cfg:
                raise ValueError('data_dir not in config file')   # todo

            pro_env.data_dir = cfg['data_dir']


if __name__ == '__main__':
    pass
