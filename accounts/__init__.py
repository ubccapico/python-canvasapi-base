from CanvasAPI.util import callhelper
from CanvasAPI.accounts import sub_accounts
from CanvasAPI import instance

__all__ = ["get", "sub_accounts"]

def get(account_id):
    '''Gets a course'''
    url_str = "accounts/{}".format(account_id)
    return instance.call_api(url_str)
