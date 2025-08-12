import datetime
from django.utils.deprecation import MiddlewareMixin

class VisitorLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        path = request.path
        print(f"[{datetime.datetime.now()}] IP: {ip}, Device: {user_agent}, Path: {path}")

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
