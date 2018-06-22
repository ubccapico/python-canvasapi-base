from CanvasAPI import instance
from CanvasAPI.util import callhelper

__all__ = ["get"]

def get(user_id, *args):
    '''List enrollments'''
    url_str = "users/{}/enrollments{}".format(user_id, callhelper.args_to_params(*args))
    return instance.all_pages(url_str)

