import falcon
from auth.config import getLogger
from auth.middleware.auth0 import AuthMiddleware
from auth.resources.login import LoginResource
from auth.resources.quote import QuoteResource

log = getLogger(__name__)
api = falcon.API(middleware=[AuthMiddleware()])
api.req_options.auto_parse_form_urlencoded = True
api.add_route('/callback', LoginResource())
api.add_route('/api/quote', QuoteResource())