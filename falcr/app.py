import falcon
from falcr.config import getLogger
from falcr.middleware.auth0 import AuthMiddleware
from falcr.resources.quote import QuoteResource
from falcr.db.ndb_load import init_data, test_data

log = getLogger(__name__)

init_data()
test_data()

api = falcon.API(middleware=[AuthMiddleware()])
api.req_options.auto_parse_form_urlencoded = True
api.add_route('/quote', QuoteResource())

