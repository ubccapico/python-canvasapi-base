from CanvasAPI import instance
from CanvasAPI.util import callhelper

__all__ = ["get", "post", "delete", "reactivate"]

def get(course_id, *args):
    '''List enrollments'''
    url_str = "courses/{}/enrollments{}".format(course_id, callhelper.args_to_params(*args))
    return instance.all_pages(url_str)


def post(course_id, user_id, post_fields={}):
    '''Enroll a user

        Keyword Arguments:
        course_id - id of course
        post_fields: - fields to post
            enrollment[type] : string
            enrollment[role] : string
            enrollment[role_id] : integer
            enrollment[enrollment_state] : string (active, invited, inactive)
            enrollment[limit_privileges_to_course_section] : boolean
            enrollment[notify] : boolean
    '''
    post_fields['enrollment[user_id]'] = user_id
    url_str = "courses/{}/enrollments".format(course_id)
    return instance.call_api(url_str, method="POST", post_fields=post_fields)

def delete(course_id, enrollment_id, task="delete"):
    '''Conclude, deactivate, or delete an enrollment'''
    url_str = "courses/{}/enrollments/{}?task={}".format(course_id, enrollment_id, task)
    return instance.call_api(url_str, method="DELETE")

def reactivate(course_id, enrollment_id):
    '''Re-activate an enrollment'''
    url_str = "courses/{}/enrollments/{}/reactivate".format(course_id, enrollment_id)
    return instance.call_api(url_str, method="PUT")
