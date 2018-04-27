from CanvasAPI import instance
from CanvasAPI.util import callhelper

__all__ = ["get", "put"]

def get(course_id, *args):
    '''Gets course settings'''
    url_str = "courses/{}/settings{}".format(course_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)

def put(course_id, post_fields, *args):
    '''Updates course settings

        Keyword arguments:
        course_id - id of course to update
        post_fields - a dict of fields to update
            - allow_student_discussion_topics : boolean
            - allow_student_forum_attachments : boolean
            - allow_student_discussion_editing : boolean
            - allow_student_organized_groups : boolean
            - hide_final_grades : boolean
            - hide_distribution_graphs : boolean
            - lock_all_announcements : boolean
            - restrict_student_past_view : boolean
            - restrict_student_future_view : boolean
            - show_announcements_on_home_page : boolean
            - home_page_announcement_limit : integer
    '''
    url_str = "courses/{}/settings{}".format(course_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str, method="PUT", post_fields=post_fields)

