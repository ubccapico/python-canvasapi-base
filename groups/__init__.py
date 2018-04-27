from CanvasAPI.util import callhelper
from CanvasAPI.courses import settings, users
from CanvasAPI import instance

__all__ = ["get"]


def get(group_id, *args):
    '''Gets a course'''
    url_str = "groups/{}{}".format(group_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)
