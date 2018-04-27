from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get", "get_question", "put_question", "post_question", "delete_question"]


def get(course_id, quiz_id, *args):
    '''List questions in a quiz or a submission'''
    url_str = "courses/{}/quizzes/{}/questions{}".format(course_id, quiz_id, callhelper.args_to_params(*args))
    return instance.all_pages(url_str)

def get_question(course_id, quiz_id, question_id, *args):
    '''Get a single quiz question'''
    url_str = "courses/{}/quizzes/{}/questions/{}{}".format(course_id, quiz_id, question_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)

def put_question(course_id, quiz_id, question_id, post_fields):
    '''Updates an existing quiz question for this quiz
            question[question_name] : string
            question[question_text] : string
            question[quiz_group_id] : integer
            question[question_type] : string
            question[position] : integer
            question[points_possible] : integer
            question[correct_comments] : string
            question[incorrect_comments] : string
            question[neutral_comments] : string
            question[text_after_answers] : string
            question[answers] : Model
            '''
    url_str = "courses/{}/quizzes/{}/questions/{}".format(course_id, quiz_id, question_id)
    return instance.call_api(url_str, method="PUT", post_fields=post_fields)

def post_question(course_id, quiz_id, post_fields):
    '''Create a single quiz question
            question[question_name] : string
            question[question_text] : string
            question[quiz_group_id] : integer
            question[question_type] : string
            question[position] : integer
            question[points_possible] : integer
            question[correct_comments] : string
            question[incorrect_comments] : string
            question[neutral_comments] : string
            question[text_after_answers] : string
            question[answers] : Model
            '''
    url_str = "courses/{}/quizzes/{}/questions".format(course_id, quiz_id)
    return instance.call_api(url_str, method="POST", post_fields=post_fields)

def delete_question(course_id, quiz_id, question_id):
    '''Deletes a question'''
    url_str = "courses/{}/quizzes/{}/questions/{}".format(course_id, quiz_id, question_id)
    return instance.call_api(url_str, method="DELETE")
