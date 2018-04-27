from CanvasAPI.util import callhelper
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import urllib
import collections
import logging


class Instance:
    @property
    def server_url(self):
        return self._server_url
    @server_url.setter
    def server_url(self, value):
        self._server_url = value
    @property
    def token(self):
        return self._token
    @token.setter
    def token(self, value):
        self._token = value
    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, value):
        self._version = value

    @property
    def initialized(self):
        ##Check whether _server_url and _token are None or empty
        return not (not self._server_url or not self._token)

    def __init__(self, server_url="", token="", version="v1"):
        self.connect(server_url, token, version)

    def connect(self, server_url, token, version="v1"):
        self._server_url = server_url
        self._token = token
        self._version = version

    def call_api(self, url, method="GET", is_URL_absolute=False, post_fields=None):
        response = self._call_api_raw(url, method=method, is_URL_absolute=is_URL_absolute, post_fields=post_fields)
        if response is not None:
            return callhelper.get_response_body(response)
        else:
            return None

        
    def _call_api_raw(self, url, method="GET", is_URL_absolute=False, post_fields=None):
        '''Makes an API call, returning up to 10 results.

        Keyword arguments:
        url - url to call (example "courses")
        method - the API method (default "GET")
               - optionally, "GET, POST, PUT, DELETE"
        is_URL_absolute - whether the given URL is absolute, or
                          uses the given server (default False)
        post_fields - set of terms to include in a post call (default None)
        '''

        if not self.initialized:
            raise ValueError("Instance must be initialized before making a call")
        
        server_url = self.server_url
        version = self.version
        token = self._token
        
        if is_URL_absolute:
            urlstr = url
        else:
            urlstr = 'https://{}/api/{}/{}'.format(server_url, version, url)
            
        request = Request(urlstr)
        request.add_header('Authorization', 'Bearer {}'.format(token))
        request.method = method
        if post_fields is not None:
            request.data = urlencode(post_fields).encode()

        
        try:
            r = urlopen(request) 
        except urllib.error.HTTPError as e:
            if post_fields is not None:
                logging.warning("HTTP Error {} '{}': urlstr='{}' method='{}' post_fields='{}'".format(e.code, e.reason, urlstr, method, ", ".join(["{}:{}".format(key, value) for key, value in post_fields.items()])))
            else:
                logging.warning("HTTP Error {} '{}': urlstr='{}' method='{}'".format(e.code, e.reason, urlstr, method))       
            r = None
        return r


    def _pages(self, url, method="GET", is_URL_absolute=False, post_fields=None):
        '''Gets an iteratable return of all results of an API call

        Keyword arguments:
        url - url to call (example "courses")
        method - the API method (default "GET")
               - optionally, "GET, POST, PUT, DELETE"
        is_URL_absolute - whether the given URL is absolute, or
                          uses the given server (default False)
        post_fields - set of terms to include in a post call (default None)
        '''
        response = self._call_api_raw(url, method, is_URL_absolute, post_fields)
        yield response
        more_pages = True
        while more_pages:
            link_header = None
            for header in response.headers.items():
                if header[0] == 'Link':
                    link_header = header
                    break
            else:
                more_pages = False
                raise StopIteration()
            links = link_header[1].split(',')
            for link in links:
                parts = link.split(';')
                if parts[1].find('next') >= 0:
                    next_page = parts[0]
                    next_page = next_page.replace('<', '')
                    next_page = next_page.replace('>', '')
                    next_page = next_page.strip()
                    response = self._call_api_raw(url=next_page, method=method, is_URL_absolute=True, post_fields=None)
                    yield response
                    break
            else:
                more_pages = False
                raise StopIteration()

    def all_pages(self, url, method="GET", is_URL_absolute=False, post_fields=None):
        '''Makes an API call, returning all results.

        Keyword arguments:
        url - url to call (example "courses")
        method - the API method (default "GET")
               - optionally, "GET, POST, PUT, DELETE"
        is_URL_absolute - whether the given URL is absolute, or
                          uses the given server (default False)
        post_fields - set of terms to include in a post call (default None)
        '''
        collector = []
        for response in self._pages(url, method, is_URL_absolute, post_fields):
            response_body = callhelper.get_response_body(response)
            if isinstance(response_body, collections.OrderedDict):
                response_body = [response_body]
            collector = collector + response_body
        return collector
