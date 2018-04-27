from CanvasAPI.util import callhelper
from CanvasAPI.custom_gradebook_columns import data
from CanvasAPI import instance

__all__ = ["get", "post", "put", "delete", "data"]


def get(course_id, *args):
    '''List custom gradebook columns'''
    url_str = "courses/{}/custom_gradebook_columns{}".format(course_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)

def post(course_id, column_title):
    '''Create a custom gradebook column'''
    url_str = "courses/{}/custom_gradebook_columns".format(course_id)
    return instance.call_api(url_str, method="POST", post_fields={"column[title]":column_title})

def put(course_id, column_id, column_title):
    '''Update a custom gradebook column'''
    url_str = "courses/{}/custom_gradebook_columns/{}".format(course_id, column_id)
    return instance.call_api(url_str, method="PUT", post_fields={"column[title]":column_title})

def delete(course_id, column_id):
    '''Delete a custom gradebook column'''
    url_str = "courses/{}/custom_gradebook_columns/{}".format(course_id, column_id)
    return instance.call_api(url_str, method="DELETE")
