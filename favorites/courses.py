from CanvasAPI import instance

__all__ = ["get", "post", "delete", "reset"]

def get():
    '''List favorite courses'''
    url_str = "users/self/favorites/courses"
    return instance.all_pages(url_str)

def post(course_id):
    '''Add course to favorites'''
    url_str = "users/self/favorites/courses/{}".format(course_id)
    return instance.call_api(url_str, method="POST")

def delete(course_id):
    '''Add course to favorites'''
    url_str = "users/self/favorites/courses/{}".format(course_id)
    return instance.call_api(url_str, method="DELETE")

def reset():
    '''Reset course favourites'''
    url_str = "users/self/favorites/courses"
    return instance.call_api(url_str, method="DELETE")
