import falcon
from falcr.config import getLogger
from falcr.db import model, auth

log = getLogger(__name__)


class LoginResource(object):
    def on_post(self, req, resp):
        log.info("/login got on_post")
        log.info("req.media=%r", req.media)
        email = req.media.get('email')
        password = req.media.get('password')
        user = model.AppUsers.check_user(email, password)
        if not user:
            raise falcon.HTTPUnauthorized("Unauthorized")
        resp.media = auth.get_token(user)
