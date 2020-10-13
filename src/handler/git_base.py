# -*-  coding: utf-8 -*-
"""
  Created by PeakSong on 2020/10/13.
"""
from functools import wraps

from git import Repo


def repo_validation(func):
    @wraps(func)
    def _func(*args, **kwargs):
        if not isinstance(GitWrapper.native_repo, Repo):
            raise ValueError("Native repo hasn't been inited properly")

        return func(args, kwargs)

    return _func


class GitWrapper:
    native_repo = None

    # auto generate .git when bare is False
    # 只有当bare为False时, 才自动生成.git文件夹
    @classmethod
    def init(cls, path: str, bare=False) -> Repo:
        cls.native_repo = Repo.init(path, bare=bare)
        # assert not cls.native_repo.bare

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
    def add_remote(cls, remote_url):
        pass


if __name__ == '__main__':
    GitWrapper.init('D:/git repository/git_t', bare=False)
