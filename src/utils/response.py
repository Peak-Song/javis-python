# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/10/15.
"""
from functools import wraps
from logging import getLogger

from flask import jsonify

logger = getLogger()


class ResponseUtil:
    @classmethod
    def response(cls, success=True, data=None, message=None):
        return jsonify({'success': success, 'message': message, 'data': data}), 200


def response_wrap(func):
    @wraps(func)
    def _func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return ResponseUtil.response(success=True, data=result)
        except Exception as e:
            logger.exception('error occurs')
            return ResponseUtil.response(success=False, message=str(e))

    return _func
