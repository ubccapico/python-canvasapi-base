from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get"]

def get(account_id, *args):
    '''List enrollment terms'''
    url_str = "accounts/{}/terms{}".format(account_id, callhelper.args_to_params(*args))
    return instance.all_pages(url_str)
