from CanvasAPI.util import callhelper
from CanvasAPI.files import courses
from CanvasAPI import instance

__all__ = ["get", "courses"]


def get(file_id, *args):
    '''Gets a course'''
    url_str = "files/{}{}".format(file_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)
