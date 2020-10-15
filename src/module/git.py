# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/9/28.
"""
from flask import Blueprint
from ..g import pro_env
from ..utils import response_wrap
git_module = Blueprint('git_module', __name__)


# 获取git配置信息
@git_module.route('/api/git_config', method=['GET'])
def get_git_config():
    pass


# 前端判断git是否已经正常运行
@git_module.route('/api/git_ready', method=['GET'])
@response_wrap
def git_ready():
    return {'git_ready': pro_env.git_ready}


# 保存git配置信息
@git_module.route('/api/git_config', method=['POST'])
def save_git_config():
    pass
