from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get"]

def get(account_id, recursive=False):
    '''Gets a course'''
    url_str = "accounts/{}/sub_accounts?recursive={}".format(account_id, recursive)
    return instance.all_pages(url_str)

def delete(account_id, sub_account):
    '''Delete a sub-account'''
    url_str = "accounts/{}/sub_accounts/{}".format(account_id, sub_account)
    return instance.call_api(url_str, method="DELETE")
