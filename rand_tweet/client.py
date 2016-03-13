import base64
import json
import sys

from urllib2 import urlopen, Request, HTTPError

"""
The following is basically taken from
https://github.com/pabluk/twitter-application-only-auth
"""

ENDPOINT = 'https://api.twitter.com'
REQ_TOKEN_URL = '%s/oauth2/token' % ENDPOINT

class ClientException(Exception):
    pass

class Client(object):

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.token = ''

    def req(self, url):
        if not self.token:
            self.token = self._get_token()

        req = Request(url)
        req.add_header('Authorization', 'Bearer %s' % self.token)
        try:
            res = urlopen(req)
        except HTTPError:
            raise ClientException

        data = self._get_json_obj(res)
        return data

    def _get_token(self):
        bearer_token = '%s:%s' % (self.key, self.secret)
        encoded_token = base64.b64encode(bearer_token.encode('ascii'))
        req = Request(REQ_TOKEN_URL)
        req.add_header('Content-Type',
                           'application/x-www-form-urlencoded;charset=UTF-8')
        req.add_header('Authorization',
                           'Basic %s' % encoded_token.decode('utf-8'))

        request_data = 'grant_type=client_credentials'.encode('ascii')
        req.data = request_data

        res = urlopen(req)
        data = self._get_json_obj(res)
        return data['access_token']

    def _get_json_obj(self, res):
        server_data = res.read().decode('utf-8')
        data = json.loads(server_data)
        return data
