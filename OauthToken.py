
"""class to generate and return oauth2 token from idcs service"""

__author__ = "Andrew Downing"
__version__ = "0.1"

import requests
import time


class OctoToken(object):
    """
    Class for generating authentication tokens
    * dont add your client id or secret to the code.  Pass them into the constructor
    """"
    def __init__(self, client_id=None, client_secret=None, oauth_uri=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_uri = oauth_uri
        self.grant_token = None
        self.expires = 0
        self.grant_type = 'client_credentials'
        self.scope = "urn:opc:idm:__myscopes__"
        
    def __repr__(self):
        """
        Print object details
        Returns:

        """
        return '{self.__class__.__name__}({self.client_id},{self.oauth_uri},{self.grant_token})'.format(self=self)

    def get_token(self):
        """
        If time limit is past expiry, get new token, else returns current token
        Returns: (str): token

        """
        if self.expires < int(time.time()):
            return self._gen_token()
        else:
            return self.grant_token

    def _gen_token(self):
        """
        Helper method to format server request and set token expiry
        Returns:  (str): token

        """
        body_params = {'grant_type': self.grant_type, 'scope': self.scope}
        self.grant_token = requests.post(self.oauth_uri,
                                         data=body_params,
                                         auth=(self.client_id, self.client_secret)).json()
        self.expires = time.time() + 3600

        return self.grant_token
