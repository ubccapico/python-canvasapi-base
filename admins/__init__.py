from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["get", "post", "delete"]

def get(account_id):
    '''List account admins'''
    url_str = "accounts/{}/admins".format(account_id)
    return instance.all_pages(url_str)

def post(account_id, user_id, role_id):
    '''Make an account admin'''
    url_str = "accounts/{}/admins".format(account_id)
    post_fields = {"user_id":user_id, "role_id":role_id}
    return instance.call_api(url_str, method="POST", post_fields=post_fields)

def delete(account_id, user_id):
    '''Remove account admin'''
    url_str = "accounts/{}/admins/{}".format(account_id, user_id)
    return instance.call_api(url_str, method="DELETE")
