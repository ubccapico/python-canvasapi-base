from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get", "get_current", "get_completed"]

def get(account_id, term_id):
    '''Get department-level grade data'''
    url_str = "accounts/{}/analytics/terms/{}/grades".format(account_id, term_id)
    return instance.all_pages(url_str)

def get_current(account_id):
    '''Get department-level grade data'''
    url_str = "accounts/{}/analytics/current/grades".format(account_id)
    return instance.all_pages(url_str)

def get_completed(account_id):
    '''Get department-level grade data'''
    url_str = "accounts/{}/analytics/completed/grades".format(account_id)
    return instance.all_pages(url_str)
