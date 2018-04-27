from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get"]

def get(course_id):
    '''List external tools'''
    url_str = "courses/{}/tabs?include[]=external".format(course_id)
    return instance.all_pages(url_str)
