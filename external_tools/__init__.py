from CanvasAPI.util import callhelper
from CanvasAPI.external_tools import courses
from CanvasAPI import instance

__all__ = ["get", "get_all_tools", "put", "courses"]

def get_all_tools(account_id, *args):
    '''List external tools'''
    url_str = "accounts/{}/external_tools{}".format(account_id, callhelper.args_to_params(*args))
    return instance.all_pages(url_str)

def get(account_id, external_tool_id):
    '''Get a single external tool'''
    url_str = "accounts/{}/external_tools/{}".format(account_id, external_tool_id)
    return instance.call_api(url_str)

def put(account_id, external_tool_id, post_fields={}):
    '''Edit an external tool'''
    url_str = "accounts/{}/external_tools/{}".format(account_id, external_tool_id)
    return self._connector.call_api(url_str, method="PUT",  post_fields=post_fields)
