from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get"]


def get(course_id, quiz_id, group_id):
    '''List questions in a quiz or a submission'''
    url_str = "courses/{}/quizzes/{}/groups/{}".format(course_id, quiz_id, group_id)
    return instance.all_pages(url_str)
