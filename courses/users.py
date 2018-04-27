import CanvasAPI
from CanvasAPI.util import callhelper

__all__ = ["get", "get_user", "search"]

def get(course_id, *args):
    '''List users in course'''
    url_str = "courses/{}/users{}".format(course_id, callhelper.args_to_params(*args))
    return CanvasAPI.instance.all_pages(url_str)

def get_user(course_id, user_id):
    '''Get single user'''
    url_str = "courses/{}/users/{}".format(course_id, user_id)
    return CanvasAPI.instance.call_api(url_str)

def search(course_id, search_term, *args):
    '''List users in course'''
    args = ("search_term={}".format(search_term),) + args
    url_str = "courses/{}/users{}".format(course_id, callhelper.args_to_params(*args))
    return CanvasAPI.instance.call_api(url_str)
