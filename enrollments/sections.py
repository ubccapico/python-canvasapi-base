from CanvasAPI import instance
from CanvasAPI.util import callhelper

__all__ = ["get", "post"]

def get(section_id, *args):
    '''List enrollments'''
    url_str = "sections/{}/enrollments{}".format(section_id, callhelper.args_to_params(*args))
    return instance.all_pages(url_str)


def post(section_id, user_id, post_fields={}):
    '''Enroll a user

        Keyword Arguments:
        course_id - id of course
        post_fields: - fields to post
            enrollment[type] : string
            enrollment[role] : string
            enrollment[rolle_id] : integer
            enrollment[enrollment_state] : string (active, invited, inactive)
            enrollment[limit_privileges_to_course_section] : boolean
            enrollment[notify] : boolean
    '''
    post_fields['enrollment[user_id]'] = user_id
    url_str = "sections/{}/enrollments".format(section_id)
    return instance.call_api(url_str, method="POST", post_fields=post_fields)
