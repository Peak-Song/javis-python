# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/9/28.
"""
from flask import Blueprint

doc_module = Blueprint('doc_module', __name__)


# 获取文档内容
@doc_module.route('/api/fetch_file', method=['GET'])
def fetch_file():
    pass


# 暂存文档内容, 前端每隔一段时间会暂存文档
@doc_module.route('/api/storage_file', method=['POST'])
def storage_file():
    pass


# 保存文档内容, 并推送远端
@doc_module.route('/api/save_file', method=['POST'])
def save_file():
    pass
