import falcon
from auth.config import getLogger

log = getLogger(__name__)

class LoginResource(object):
    disable_auth = True

    def on_get(self, req, resp):
        # email = req.media.get('email')
        # password = req.media.get('password')
        # user = model.check_user(email, password)
        # if not user: raise falcon.HTTPUnauthorized("Unauthorized")
        # resp.media = auth.get_token(user)
        resp.media = {'foo': 'bar'}
