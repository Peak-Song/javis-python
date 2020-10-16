# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/9/27.
  定时任务工作类, 从远端同步信息
"""
from logging import getLogger

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler

_logger = getLogger()


class Worker:
    def __init__(self):
        self.scheduler = BackgroundScheduler(executors={'default': ThreadPoolExecutor(2)}, timezone='Asia/Shanghai')

    def start(self):
        self.scheduler.start()

    def git_health_check(self):
        pass

    # 从远端同步文件目录等信息
    @classmethod
    def sync_from_remote(cls):
        pass

