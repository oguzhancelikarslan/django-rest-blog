from rest_framework.throttling import SimpleRateThrottle

class RegisterThrottle(SimpleRateThrottle):
    scope = 'registerthrottle'
    
    def get_cache_key(self, request, view):
        if request.user.is_authenticated or request.method == 'GET':
            return None  # Only throttle unauthenticated requests.

        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request)
        }