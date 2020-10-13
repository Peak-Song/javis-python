# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/10/13.
  设置程序相关的初始化变量
"""
import platform
from flask import g

my_os = platform.system()

if my_os == 'Windows':
    g.config_base = ''
    g.log_base = ''
elif my_os == 'Linux':
    g.config_base = ''
    g.log_base = ''
else:
    g.config_base = ''
    g.log_base = ''
