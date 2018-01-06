import base64
import json
from jose import jwt
import requests
import requests_toolbelt.adapters.appengine

import falcon
from falcr.config import getLogger
from falcr.db.auth import valid_token
from falcr.resources.static import StaticResource

requests_toolbelt.adapters.appengine.monkeypatch()
log = getLogger(__name__)

AUTH0_DOMAIN = 'ariftek.auth0.com'
API_AUDIENCE = 'H6L6IkdiJsZSVMkn7FljrjaAr11dIVLh'
JWKS = requests.get('https://{}/.well-known/jwks.json'.format(AUTH0_DOMAIN)).json()
RSA_KEY = dict((k, JWKS['keys'][0][k]) for k in ('kty', 'kid', 'use', 'n', 'e'))


class Unauthorized(falcon.HTTPUnauthorized):
    def __init__(self, code, description):
        super(Unauthorized, self).__init__(code, description)


class BadRequest(falcon.HTTPBadRequest):
    def __init__(self, code, description):
        super(BadRequest, self).__init__(code, description)


class AuthMiddleware(object):
    def process_resource(self, req, resp, resource, params):
        log.info("called auth middleware")
        if getattr(resource, 'disable_auth', False):
            return
        auth = req.get_header('Authorization')
        log.info("Authorization header = %r", auth)
        if not auth:
            raise Unauthorized(
                'authorization_header_missing',
                "Authorization header is expected"
            )
        parts = auth.split()
        if parts[0].lower() != 'bearer':
            raise Unauthorized(
                'invalid_header',
                "Authorization header must start with Bearer"
            )
        elif len(parts) == 1:
            raise Unauthorized(
                'invalid_header',
                "Token not found"
            )
        elif len(parts) > 2:
            raise Unauthorized(
                'invalid_header',
                "Authorization header must be Bearer token"
            )
        claims = parts[1].split('.')[1]
        if len(claims)%4 != 0:
            claims += '='*(4 - len(claims)%4)
        claims = json.loads(base64.b64decode(claims))
        log.info("claims=%r", claims)
        token = parts[1]
        try:
            payload = jwt.decode(
                token,
                RSA_KEY,
                algorithms=['RS256'],
                audience=API_AUDIENCE
            )
            log.info("payload=%r")
        except jwt.ExpiredSignatureError:
            log.exception("expired signature")
            raise Unauthorized('token_expired', "Token is expired")
        except jwt.JWTClaimsError as e:
            log.exception("invalid_claims")
            raise Unauthorized('invalid_claims', "Incorrect claims, please check the audience and issuer")
        except Exception:
            log.exception("exception")
            raise BadRequest('invalid_header', "Unable to parse authentication token.")
