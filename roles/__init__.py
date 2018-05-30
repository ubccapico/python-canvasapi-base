from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get"]

def get(account_id):
    '''Gets a course'''
    url_str = "accounts/{}/roles".format(account_id)
    return instance.all_pages(url_str)
