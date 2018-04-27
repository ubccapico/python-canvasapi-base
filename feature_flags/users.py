from CanvasAPI import instance

__all__ = ["get_all_features", "get_enabled_features", "get", "put"]

def get_all_features(user_id):
    '''List features'''
    url_str = "users/{}/features".format(user_id)
    return instance.all_pages(url_str)

def get_enabled_features(user_id):
    '''List enabled features'''
    url_str = "users/{}/features/enabled".format(user_id)
    return instance.all_pages(url_str)

def get(user_id, feature):
    '''Get feature flag'''
    url_str = "users/{}/features/{}".format(user_id, feature)
    return instance.call_api(url_str)

def put(user_id, feature, state):
    '''Set feature flag'''
    url_str = "users/{}/features/flags/{}".format(user_id, feature)
    return instance.call_api(url_str, method="PUT", post_fields={"state":state})
