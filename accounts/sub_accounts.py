from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get"]

def get(account_id, recursive=False):
    '''Gets a course'''
    url_str = "accounts/{}/sub_accounts?recursive={}".format(account_id, recursive)
    return instance.all_pages(url_str)
