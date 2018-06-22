from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get", "get_current", "get_completed"]

def get(account_id, term_id):
    '''Get department-level statistics'''
    url_str = "accounts/{}/analytics/terms/{}/statistics".format(account_id, term_id)
    return instance.call_api(url_str)

def get_current(account_id):
    '''Get department-level statistics'''
    url_str = "accounts/{}/analytics/current/statistics".format(account_id)
    return instance.call_api(url_str)

def get_completed(account_id):
    '''Get department-level statistics'''
    url_str = "accounts/{}/analytics/completed/statistics".format(account_id)
    return instance.call_api(url_str)
