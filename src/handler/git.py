# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/10/13.
  对外的git操作接口
"""

from .git_base import GitWrapper
from ..g import pro_env


class GitHandler:
    # 检查git仓库的合法性
    @classmethod
    def health_check(cls):
        pass

    @classmethod
    def init(cls):
        GitWrapper.init(pro_env.data_dir)

    # 配置git仓库
    @classmethod
    def add_remote(cls, init=False, native_working_dir='', remote_working_dir=''):
        pass

    @classmethod
    def get_remote(cls):
        pass

    @classmethod
    def git_remote_ready(cls):
        pass
