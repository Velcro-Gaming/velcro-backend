from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'api', 'engine.urls.api', name='api'),
    host(r'admin', 'engine.urls.admin', name='admin'),
)
