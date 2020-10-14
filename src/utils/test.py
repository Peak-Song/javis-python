# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/10/13.
"""
from functools import wraps


def validation(func):
    @wraps(func)
    def _func(*args, **kwargs):
        if not isinstance('123', str):
            raise ValueError("native repo hasn't been inited properly")

        return func(*args, **kwargs)

    return _func


@validation
def ttt():
    print('haha')


ttt()
