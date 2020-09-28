from flask import g

g.pro_env = {
    'git_ready': False,  # 判断git环境是否已经可以正常运行
    'data_dir': ''       # 获取当前的数据目录
}


def get_git_ready() -> bool:
    return g.pro_env['git_ready']


def set_git_ready(ready: bool):
    g.pro_env['git_ready'] = ready


def get_data_dir() -> str:
    return g.pro_env['data_dir']


def set_data_dir(data_dir: str):
    g.pro_env['data_dir'] = data_dir
