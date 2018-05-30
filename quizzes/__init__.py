from CanvasAPI.util import callhelper
from CanvasAPI.quizzes import questions, groups
from CanvasAPI import instance

__all__ = ["get", "get_quiz", "questions", "groups"]


def get(course_id, *args):
    '''List quizzes in a course'''
    url_str = "courses/{}/quizzes{}".format(course_id, callhelper.args_to_params(*args))
    return instance.all_pages(url_str)

def get_quiz(course_id, quiz_id, *args):
    '''Get a single quiz'''
    url_str = "courses/{}/quizzes/{}{}".format(course_id, quiz_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)

def put_quiz(course_id, quiz_id, post_fields, *args):
    '''Edit a quiz
        post_fields: - fields to post        
            quiz[title] : string
            quiz[description] : string
            quiz[quiz_type] : string
            quiz[assignment_group_id] : integer
            quiz[time_limit] : integer
            quiz[shuffle_answers] : boolean
            quiz[hide_results] : string
            quiz[show_correct_answers] : boolean
            quiz[show_correct_answers_last_attempt] : boolean
            quiz[show_correct_answers_at] : DateTime
            quiz[hide_correct_answers_at] : DateTime
            quiz[allowed_attempts] : integer
            quiz[scoring_policy] : string
            quiz[one_question_at_a_time] : boolean
            quiz[cant_go_back] : boolean
            quiz[access_code] : string
            quiz[ip_filter] : string
            quiz[due_at] : DateTime
            quiz[lock_at] : DateTime
            quiz[unlock_at] : DateTime
            quiz[published] : boolean
            quiz[one_time_results] : boolean
            quiz[only_visible_to_overrides] : boolean
    '''
    url_str = "courses/{}/quizzes/{}".format(course_id, quiz_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str, method="PUT", post_fields=post_fields)
