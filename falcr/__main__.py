from wsgiref.simple_server import make_server
from auth.api import api
from auth.config import getLogger
from auth.resources.static import StaticResource

log = getLogger(__name__)

if __name__ == '__main__':
    api.add_route('/', StaticResource('index.html', 'text/html; charset=utf-8'))
    api.add_route('/home', StaticResource('index.html', 'text/html; charset=utf-8'))
    api.add_route('/callback', StaticResource('index.html', 'text/html; charset=utf-8'))
    api.add_route('/dist/build.js', StaticResource('dist/build.js', 'text/javascript'))
    api.add_route('/dist/loading.svg', StaticResource('dist/loading.svg', 'image/svg+xml'))
    httpd = make_server('', 8085, api)
    httpd.serve_forever()