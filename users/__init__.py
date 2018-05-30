from CanvasAPI.util import callhelper
from CanvasAPI import instance

__all__ = ["self", "get", "search", "update_name"]

def self():
    url_str = "users/self"
    return instance.call_api(url_str)

def get(user_id, *args):
    '''Show user details'''
    url_str = "users/{}{}".format(user_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)

def update_name(user_id, full_name, sortable_name):
    '''updates a user's name'''
    url_str = "users/{}".format(user_id)
    return instance.call_api(url_str, method="PUT", post_fields={"user[name]":full_name,"user[short_name]":full_name,"user[sortable_name]":sortable_name})

def search(account_id, search_term):
    url_str = "accounts/{}/users?search_term={}".format(account_id, search_term)
    return instance.call_api(url_str)
