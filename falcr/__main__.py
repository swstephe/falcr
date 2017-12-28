from wsgiref.simple_server import make_server
from falcr.app import api
from falcr.config import getLogger, ROOT
from falcr.resources.static import StaticResource

log = getLogger(__name__)

if __name__ == '__main__':
    api.add_route('/', StaticResource('index.html', 'text/html; charset=utf-8'))
    api.add_route('/dist/build.js', StaticResource('dist/build.js', 'text/javascript'))
    httpd = make_server('', 8085, api)
    httpd.serve_forever()
