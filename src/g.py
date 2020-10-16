# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/10/13.
  设置程序相关的初始化变量
"""
import platform
from pathlib import Path

my_os = platform.system()


class ProContext:
    # 设置程序全局变量
    # program_base: 项目的基目录
    # user_home: 用户主目录
    # log_base: python日志的根目录
    def __init__(self):
        self.user_home = str(Path.home()).replace("\\", "/")
        if my_os == 'Windows':
            self.program_base = self.user_home + '/AppData/Roaming/javis/'
        elif my_os == 'Linux':
            self.program_base = self.user_home + '/.config/javis/'
        else:  # macOS
            self.program_base = self.user_home + '/Library/javis/'

        self.log_base = self.program_base + '/logs'

        self.git_native_ready = False
        self.git_remote_config = False
        self.data_dir = None


pro_env = ProContext()
