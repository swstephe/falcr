import falcon
from falcr.config import getLogger
from falcr.db.auth import valid_token
from falcr.resources.login import LoginResource
from falcr.resources.static import StaticResource

log = getLogger(__name__)


class AuthMiddleware(object):
    def process_resource(self, req, resp, resource, params):
        if isinstance(resource, (LoginResource, StaticResource)):
            return
        token = req.get_header('Authorization')
        if token and token.startswith('Bearer '):
            if valid_token(token[len('Bearer '):]):
                return
        raise falcon.HTTPUnauthorized()
