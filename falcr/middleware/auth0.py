import json
from jose import jwt
import requests
import falcon
from auth.config import getLogger

log = getLogger(__name__)
AUTH0_DOMAIN = 'ariftek.auth0.com'
API_AUDIENCE = 'https://auth.ariftek.com/'
JWKS = requests.get(
    'https://{}/.well-known/jwks.json'.format(AUTH0_DOMAIN),
    proxies={'https': 'http://stephs01:Ginger29.@neproxy:8080'},
     verify=False
).json()
RSA_KEY = dict((k, JWKS['keys'][0][k]) for k in ('kty', 'kid', 'use', 'n', 'e'))



class AuthUnauthorized(falcon.HTTPUnauthorized):
    def __init__(self, code, description):
        super(AuthUnauthorized, self).__init__(code, description)


class AuthBadRequest(falcon.HTTPBadRequest):
    def __init__(self, code, description):
        super(AuthBadRequest, self).__init__(code, description)


class AuthMiddleware(object):
    def process_resource(self, req, resp, resource, praams):
        log.info("process_resource")
        if getattr(resource, 'disable_auth', False):
            log.info("auth disabled")
            return
        auth = req.get_header('Authorization')
        log.info("auth = %r", auth)
        if not auth:
            raise AuthUnauthorized(
                'authorization_header_missing',
                "Authorization header is expected"
            )
        parts = auth.split()
        log.info("parts = %r", parts)
        if parts[0].lower() != 'bearer':
            raise AuthUnauthorized(
                'invalid_header',
                "Authorization header must start with Bearer"
            )
        elif len(parts) == 1:
            raise AuthUnauthorized(
                'invalid_header',
                "Token not found"
            )
        elif len(parts) > 2:
            raise AuthUnauthorized(
                'invalid_header',
                "Authorization header must be Bearer token"
            )
        token = parts[1]
        log.info("token=%r", token)
        try:
            payload = jwt.decode(
                token,
                RSA_KEY,
                algorithms=['RS256'],
                audience=API_AUDIENCE,
                issuer='https://{}/'.format(AUTH0_DOMAIN)
            )
            log.info("payload=%r", payload)
        except jwt.ExpiredSignatureError:
            raise AuthUnauthorized('token_expired', 'token in expired')
        except jwt.JWTClaimsError:
            raise AuthUnauthorized('invalid_claims', "incorrect claims, please check the audience and issuer")
        except Exception:
            raise AuthBadRequest('invalid_header', "Unable to parse authentication token.")
