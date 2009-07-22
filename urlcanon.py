from django.http import get_host, HttpResponsePermanentRedirect

class URLCanonicalizationMiddleware:
    def process_view(self, request, view_func, view_args, view_kwargs):
        protocol = 'https://' if request.is_secure() else 'http://'
        host = get_host(request)
        if len(host.split('.')) == 2 and not host.startswith('localhost'):
            new_url = protocol + 'www.' + host + request.get_full_path()
            return HttpResponsePermanentRedirect(new_url)
