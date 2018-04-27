from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get", "delete", "cross_list_section"]


def get(section_id, *args):
    '''Get section information'''
    url_str = "sections/{}{}".format(section_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)

def delete(section_id):
    '''Delete a section'''
    url_str = "sections/{}".format(section_id)
    return instance.call_api(url_str, method="DELETE")

def cross_list_section(section_id, new_course_id):
    '''Cross-list a Section'''
    url_str = "sections/{}/crosslist/{}".format(section_id, new_course_id)
    return instance.call_api(url_str, method="POST")
    
