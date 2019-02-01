
"""class to generate and return oauth2 token from idcs service"""

__author__ = "Andrew Downing"
__version__ = "0.1"

import requests
import time


class OctoToken(object):
    
    def __init__(self, client_id=None, client_secret=None, oauth_uri=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_uri = ouath_uri
        self.grant_token = None
        self.expires = 0
        self.grant_type = 'client_credentials'
        self.scope = "urn:opc:idm:__myscopes__"
        
    def __repr__(self):
        return '{self.__class__.__name__}({self.client_id},{self.oauth_uri},{self.grant_token})'.format(self=self)

    def get_token(self):
        if self.expires < int(time.time()):
            return self._gen_token()
        else:
            return self.grant_token

    def _gen_token(self):
        body_params = {'grant_type': self.grant_type, 'scope': self.scope}
        self.grant_token = requests.post(self.oauth_uri,
                                         data=body_params,
                                         auth=(self.client_id, self.client_secret)).json()
        self.expires = time.time() + 3600

        return self.grant_token
