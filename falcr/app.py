import falcon
from falcr.config import getLogger
from falcr.middleware.auth import AuthMiddleware
from falcr.resources.login import LoginResource
from falcr.resources.quote import QuoteResource

log = getLogger(__name__)
api = falcon.API(middleware=[AuthMiddleware()])
api.req_options.auto_parse_form_urlencoded = True
api.add_route('/login', LoginResource())
api.add_route('/quote', QuoteResource())

