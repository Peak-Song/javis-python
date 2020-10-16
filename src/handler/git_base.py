# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/10/13.
  封装大多数git仓库操作
"""
from functools import wraps

import os
from git import Repo
from git.repo.fun import is_git_dir


def repo_validation(func):
    @wraps(func)
    def _func(*args, **kwargs):
        if not isinstance(GitWrapper.native_repo, Repo):
            raise ValueError("Native repo hasn't been inited properly")

        return func(args, kwargs)

    return _func


class GitWrapper:
    native_repo: Repo = None

    @classmethod
    def init(cls, path: str):
        git_path = '%s/.git' % path
        if os.path.exists(git_path) and is_git_dir(git_path):
            cls.native_repo = Repo(path)
        else:
            # auto generate .git when bare is False
            # 只有当bare为False时, 才自动生成.git文件夹
            cls.native_repo = Repo.init(path, bare=False)

    @classmethod
    @repo_validation
    def commit(cls):
        pass

    @classmethod
    @repo_validation
    def delete(cls):
        pass

    @classmethod
    @repo_validation
    def push(cls):
        pass

    @classmethod
    @repo_validation
    def pull(cls):
        pass

    @classmethod
    @repo_validation
    def add_remote(cls, remote_name, remote_url):
        cls.native_repo.create_remote(name=remote_name, url=remote_url)

    @classmethod
    @repo_validation
    def is_native_ready(cls):
        pass

    @classmethod
    @repo_validation
    def is_remote_config(cls):
        return len(cls.native_repo.remotes) != 0  # todo


if __name__ == '__main__':
    GitWrapper.init('D:/git repository/git_t')
