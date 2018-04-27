from CanvasAPI import instance

__all__ = ["get_all_features", "get_enabled_features", "get", "put"]

def get_all_features(course_id):
    '''List features'''
    url_str = "courses/{}/features".format(course_id)
    return instance.all_pages(url_str)

def get_enabled_features(course_id):
    '''List enabled features'''
    url_str = "courses/{}/features/enabled".format(course_id)
    return instance.all_pages(url_str)

def get(course_id, feature):
    '''Get feature flag'''
    url_str = "courses/{}/features/{}".format(course_id, feature)
    return instance.call_api(url_str)

def put(course_id, feature, state):
    '''Set feature flag'''
    url_str = "courses/{}/features/flags/{}".format(course_id, feature)
    return instance.call_api(url_str, method="PUT", post_fields={"state":state})
