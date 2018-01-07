import falcon
from falcr.config import getLogger
from falcr.middleware.auth0 import AuthMiddleware
from falcr.resources.quote import QuoteResource

log = getLogger(__name__)

api = falcon.API(middleware=[AuthMiddleware()])
api.req_options.auto_parse_form_urlencoded = True
api.add_route('/quote', QuoteResource())

