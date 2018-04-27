import collections, json, re

# Some regexes for dealing with HTTP responses from API
JSON_PATTERN = re.compile(r'application/json', re.I)
CHARSET_PATTERN = re.compile(r'charset=(.+?)(;|$)')

def check_JSON(response):
    '''checks whether a response is JSON'''
    content = response.headers.get('Content-Type')
    return bool(JSON_PATTERN.search(content))

def get_Charset(response):
    '''Gets the charset of an API response'''
    content = response.headers.get('Content-Type')
    return CHARSET_PATTERN.search(content).group(1)

def get_response_body(response):
    '''Converts an API response into a readable format'''
    charset = get_Charset(response)
    response_body = response.readline().decode(charset)
    is_JSON = check_JSON(response)
    if is_JSON:
        response_body = json.loads(response_body, object_pairs_hook=collections.OrderedDict)
    return response_body

def args_to_params(*args):
    '''Converts  arguments "?xxx&yyy" format.'''
    if len(args) <= 0:
        return ""
    return "?"+ '&'.join(["{}".format(args[i]) for i in range(0, len(args))])
