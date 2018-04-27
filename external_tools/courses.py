from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get", "get_all_tools", "put"]

def get_all_tools(course_id, *args):
    '''List external tools'''
    url_str = "courses/{}/external_tools{}".format(course_id, callhelper.args_to_params(*args))
    return instance.all_pages(url_str)

def get(course_id, external_tool_id):
    '''Get a single external tool'''
    url_str = "courses/{}/external_tools/{}".format(course_id, external_tool_id)
    print(url_str)
    return instance.call_api(url_str)

def put(course_id, external_tool_id, post_fields={}):
    '''Edit an external tool'''
    url_str = "courses/{}/external_tools/{}".format(course_id, external_tool_id)
    return instance.call_api(url_str, method="PUT",  post_fields=post_fields)
