from CanvasAPI.util import callhelper
from CanvasAPI.courses import settings, users
from CanvasAPI import instance

__all__ = ["get_history", "get_student_history", "get_grader_history"]


def get_course(course_id):
    '''Gets a course'''
    url_str = "audit/grade_change/courses/{}?include[]=current_grade".format(course_id)
    return instance.call_api(url_str)

def get_student(course_id, student_id):
    '''Gets a course'''
    url_str = "audit/grade_change/courses/{}/students/{}?include[]=current_grade".format(course_id, student_id)
    return instance.call_api(url_str)

def get_grader(course_id, grader_id):
    '''Gets a course'''
    url_str = "audit/grade_change/courses/{}/graders/{}?include[]=current_grade".format(course_id, grader_id)
    return instance.call_api(url_str)
