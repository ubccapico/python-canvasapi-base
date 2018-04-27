from CanvasAPI.util import callhelper
from CanvasAPI.courses import settings, users
from CanvasAPI import instance

__all__ = ["get", "get_sections", "put", "settings", "users"]


def get(course_id, *args):
    '''Gets a course'''
    url_str = "courses/{}{}".format(course_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)

def get_sections(course_id, *args):
    '''Gets a course'''
    url_str = "courses/{}/sections{}".format(course_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str)

def put(course_id, post_fields, *args):
    '''Updates a course

        Keyword Arguments:
        course_id - id of course
        post_fields: - fields to post
            course[account_id] : integer
            course[name] : string
            course[course_code] : string
            course[start_at] : DateTime
            course[end_at] : DateTime
            course[license] : string
            course[is_public] : boolean
            course[is_public_to_auth_users] : boolean
            course[public_syllabus] : boolean
            course[public_syllabus_to_auth] : boolean
            course[public_description] : string
            course[allow_student_wiki_edits] : boolean
            course[allow_wiki_comments] : boolean
            course[allow_student_forum_attachments] : boolean
            course[open_enrollment] : boolean
            course[self_enrollment] : boolean
            course[restrict_enrollments_to_course_dates] : boolean
            course[term_id] : integer
            course[sis_course_id] : string
            course[integration_id] : string
            course[hide_final_grades] : boolean
            course[time_zone] : string
            course[apply_assignment_group_weights] : boolean
            course[storage_quota_mb] : integer
            offer : boolean
            course[event] : string
            course[default_view] : string
            course[syllabus_body] : string
            course[grading_standard_id] : integer
            course[course_format] : string
            course[image_id] : integer
            course[image_url] : string
            course[remove_image] : boolean
            course[blueprint] : boolean
            course[blueprint_restrictions] : BlueprintRestriction
            course[use_blueprint_restrictions_by_object_type] : boolean
            course[blueprint_restrictions_by_object_type] : multiple BlueprintRestrictions
    '''
    url_str = "courses/{}{}".format(course_id, callhelper.args_to_params(*args))
    return instance.call_api(url_str, method="PUT", post_fields=post_fields)


def post(account_id, post_fields):
    '''Create a new course

        Keyword Arguments:
        course_id - id of course
        post_fields: - fields to post
            course[name] : string
            course[course_code] : string
            course[start_at] : DateTime
            course[end_at] : DateTime
            course[license] : string
            course[is_public] : boolean
            course[is_public_to_auth_users] : boolean
            course[public_syllabus] : boolean
            course[public_syllabus_to_auth] : boolean
            course[public_description] : string
            course[allow_student_wiki_edits] : boolean
            course[allow_wiki_comments] : boolean
            course[allow_student_forum_attachments] : boolean
            course[open_enrollment] : boolean
            course[self_enrollment] : boolean
            course[restrict_enrollments_to_course_dates] : boolean
            course[term_id] : integer
            course[sis_course_id] : string
            course[integration_id] : string
            course[hide_final_grades] : boolean
            course[time_zone] : string
            course[apply_assignment_group_weights] : boolean
            course[storage_quota_mb] : integer
            offer : boolean
            course[event] : string
            course[default_view] : string
            course[syllabus_body] : string
            course[grading_standard_id] : integer
            course[course_format] : string
            course[image_id] : integer
            course[image_url] : string
            course[remove_image] : boolean
            course[blueprint] : boolean
            course[blueprint_restrictions] : BlueprintRestriction
            course[use_blueprint_restrictions_by_object_type] : boolean
            course[blueprint_restrictions_by_object_type] : multiple BlueprintRestrictions
    '''
    url_str = "accounts/{}/courses".format(account_id)
    return instance.call_api(url_str, method="POST", post_fields=post_fields)


