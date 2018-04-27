from CanvasAPI import instance
from CanvasAPI.util import callhelper

__all__ = ["get", "quota"]

def get(course_id, *args):
    '''List files'''
    url_str = "courses/{}/files{}".format(course_id, callhelper.args_to_params(*args))
    return instance.all_pages(url_str)

def quota(course_id):
    '''Get quota information'''
    url_str = "courses/{}/files/quota".format(course_id)
    return instance.call_api(url_str)

def get_folders(course_id):
    '''List all folders'''
    url_str = "courses/{}/folders".format(course_id)
    return instance.call_api(url_str)
