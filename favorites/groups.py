from CanvasAPI import instance

__all__ = ["get", "post", "delete", "reset"]

def get():
    '''List favorite groups'''
    url_str = "users/self/favorites/groups"
    return instance.all_pages(url_str)

def post(group_id):
    '''Add group to favorites'''
    url_str = "users/self/favorites/groups/{}".format(group_id)
    return instance.call_api(url_str, method="POST")

def delete(group_id):
    '''Add group to favorites'''
    url_str = "users/self/favorites/groups/{}".format(group_id)
    return instance.call_api(url_str, method="DELETE")

def reset():
    '''Reset group favourites'''
    url_str = "users/self/favorites/groups"
    return instance.call_api(url_str, method="DELETE")
