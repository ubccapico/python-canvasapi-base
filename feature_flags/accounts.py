from CanvasAPI import instance

__all__ = ["get_all_features", "get_enabled_features", "get", "put"]

def get_all_features(account_id):
    '''List features'''
    url_str = "accounts/{}/features".format(account_id)
    return instance.all_pages(url_str)

def get_enabled_features(account_id):
    '''List enabled features'''
    url_str = "accounts/{}/features/enabled".format(account_id)
    return instance.all_pages(url_str)

def get(account_id, feature):
    '''Get feature flag'''
    url_str = "accounts/{}/features/{}".format(account_id, feature)
    return instance.call_api(url_str)

def put(account_id, feature, state):
    '''Set feature flag'''
    url_str = "accounts/{}/features/flags/{}".format(account_id, feature)
    return instance.call_api(url_str, method="PUT", post_fields={"state":state})
