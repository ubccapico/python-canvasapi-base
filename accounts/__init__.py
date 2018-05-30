from CanvasAPI.util import callhelper
from CanvasAPI.accounts import sub_accounts
from CanvasAPI import instance

__all__ = ["get", "sub_accounts"]

def get(account_id):
    '''Gets a course'''
    url_str = "accounts/{}".format(account_id)
    return instance.call_api(url_str)

def put(account_id, post_fields):
    url_str = "accounts/{}".format(account_id)
    return instance.call_api(url_str, method="PUT", post_fields=post_fields)

def get_settings(account_id):
    url_str = "accounts/{}".format(account_id)
    return instance.call_api(url_str)
