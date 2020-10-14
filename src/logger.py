# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/10/14.
"""
from os import path, makedirs
from sys import stdout
from logging import getLogger
from logging import DEBUG, ERROR
from logging import StreamHandler, Formatter
from logging.handlers import TimedRotatingFileHandler

from .g import pro_env

log_base_cfg = {
    'console_level': DEBUG,
    'py_log_base': path.join(pro_env.log_base, 'python').replace('\\', '/'),
    'full_file': path.join(pro_env.log_base, 'python', 'full.log').replace('\\', '/'),
    'error_file': path.join(pro_env.log_base, 'python', 'error.log').replace('\\', '/')
}

makedirs(log_base_cfg['py_log_base'], exist_ok=True)

console_format = Formatter(fmt='%(asctime)s [%(levelname)s] %(name)s-> %(message)s')
file_format = Formatter(fmt='%(asctime)s [%(levelname)s] %(name)s-> %(message)s', datefmt='%H:%M:%S')

console_level = log_base_cfg['console_level']
console_handler = StreamHandler(stream=stdout)
console_handler.setLevel(console_level)
console_handler.setFormatter(console_format)

full_handler = TimedRotatingFileHandler(filename=log_base_cfg['full_file'],
                                        when='midnight',
                                        interval=1,
                                        backupCount=30,
                                        encoding='utf-8')
full_handler.setLevel(DEBUG)
full_handler.setFormatter(file_format)
full_handler.suffix = '%Y-%m-%d.log'

error_handler = TimedRotatingFileHandler(filename=log_base_cfg['error_file'],
                                         when='midnight',
                                         interval=1,
                                         backupCount=30,
                                         encoding='utf-8')
error_handler.setLevel(ERROR)
error_handler.setFormatter(file_format)
error_handler.suffix = '%Y-%m-%d.log'

root = getLogger()
root.setLevel(DEBUG)
root.addHandler(console_handler)
root.addHandler(full_handler)
root.addHandler(error_handler)

root.info('python logging init...')
