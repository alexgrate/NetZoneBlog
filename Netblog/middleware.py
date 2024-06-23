# myapp/middleware.py
from django.utils.deprecation import MiddlewareMixin

class RemoveNoIndexForSitemapMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path == '/sitemap.xml':
            response.headers['X-Robots-Tag'] = 'index, follow'
        return response
