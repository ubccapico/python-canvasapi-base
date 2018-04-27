from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get_all"]

def get_all(course_id):
    '''list_assignments'''
    url_str = "/courses/{}/assignments".format(course_id)
    return instance.call_api(url_str)
