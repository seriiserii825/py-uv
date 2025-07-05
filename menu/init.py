from classes.Uv import Uv


def init():
    Uv.start()
    Uv.create_pyproject_toml()
    Uv.pre_commit_hook()
