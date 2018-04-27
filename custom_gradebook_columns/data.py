from CanvasAPI import instance
from CanvasAPI.util import callhelper

__all__ = ["get", "put"]

def get(course_id, column_id, *args):
    '''List entries for a column'''
    url_str = "courses/{}/custom_gradebook_columns/{}/data{}".format(course_id, column_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)

def put(course_id, column_id, user_id, column_data_content):
    '''Updates column data'''
    url_str = "courses/{}/custom_gradebook_columns/{}/data/{}".format(course_id, column_id, user_id)
    return instance.call_api(url_str, method="PUT", post_fields={"column_data[content]":column_data_content})

