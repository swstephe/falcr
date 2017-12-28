from falcr.db.model import database
from falcr.config import getLogger

log = getLogger(__name__)


class ConnectionMiddleware(object):
    def process_request(self, req, resp):
        database.connect()

    def process_response(self, req, resp, resource, req_succeeded):
        if not database.is_closed():
            database.close()
