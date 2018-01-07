import jwt
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm

import falcon
from falcr.config import getLogger

log = getLogger(__name__)
jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))

PUBKEY = """\
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvKw8S0pDTr8xUSA4pHv9
zuK4+Ml6rQ2mTw1xzK+59RGhczexNe0DguliH57ez5U+OVYq0PEE+jEfu0d+XfZs
pNRh1SL1tG1WKmrTsIZZYwNxyOYib7lLGkIxopgUU7rCbqp219LSW4EiJ8mESTRi
BmzKtgfnszmEH68FF/F93yzq6L+BXhUqqyIp0k+UNNwRvGFvzVFYxB6ePWgKsEI8
WCXoViLGfo1DoW1oTazX7MA8sVLy2zV5qE866ohC6Q4qS+3yl2XA3mCgGdmcUkzd
zY9LRBV2YMfL+8aAemHUuIl4KVrWU3lusApqDlYJxhuqgkwyaqqEyirw3/U6bN8B
8wIDAQAB
-----END PUBLIC KEY-----
"""
AUTH_CONFIG = {
    'algorithms': ['RS256'],
    'audience': 'NjYo5Wd169t0G4IPLspKBgQtjJif1cd0',
    'subject': 'H6L6IkdiJsZSVMkn7FljrjaAr11dIVLh@clients',
    'issuer': 'https://ariftek.auth0.com/'
}


class AuthMiddleware(object):
    def process_resource(self, req, resp, resource, params):
        if getattr(resource, 'disable_auth', False):
            return
        auth = req.get_header('Authorization')
        if not auth:
            raise falcon.HTTPUnauthorized(
                'authorization_header_missing',
                "Authorization header is expected"
            )
        auth = auth.split()
        if len(auth) != 2:
            raise falcon.HTTPBadRequest('bad request format', "Expected 'Bearer' Token")
        token = auth[1]
        try:
            jwt.decode(token, PUBKEY, **AUTH_CONFIG)
        except Exception as e:
            log.exception(str(e))
            raise falcon.HTTPUnauthorized(
                'invalid_claims',
                "Incorrect claims, please check the audience and issuer"
            )
