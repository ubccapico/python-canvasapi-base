from CanvasAPI.util import callhelper
from CanvasAPI.enrollments import courses, sections, users
from CanvasAPI import instance

__all__ = ["get", "courses", "sections", "users"]

def get(account_id, enrollment_id, *args):
    '''Enrollment by ID'''
    url_str = "accounts/{}/enrollments/{}".format(account_id, enrollment_id)
    return instance.call_api(url_str)
