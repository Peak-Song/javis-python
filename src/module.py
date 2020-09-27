# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/9/27.
  接受来自于前端的请求
"""
from flask import Blueprint

module = Blueprint('module', __name__)


# 返回前端文件目录的更新
@module.route('/api/update', method=['GET'])
def update():
    pass


# 获取文档内容
@module.route('/api/fetch_file', method=['GET'])
def fetch_file():
    pass


# 获取文档中的资源文件, 如图片,音频或者视频
@module.route('/api/fetch_res', method=['GET'])
def fetch_res():
    pass


# 暂存文档内容, 前端每隔一段时间会暂存文档
@module.route('/api/storage_file', method=['POST'])
def storage_file():
    pass


# 保存文档内容, 并推送远端
@module.route('/api/save_file', method=['POST'])
def save_file():
    pass


# 保存文档中的资源文件, 如图片,音频或者视频
@module.route('/api/save_res', method=['POST'])
def save_res():
    pass



