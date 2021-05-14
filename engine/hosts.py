from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns(
    '',
    # host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'api', 'engine.urls.api', name='api'),

    host(r'admin', 'engine.urls.admin', name='admin'),

    # host(r'dashboard', 'dashboard.urls', name='dashboard'),
    # host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
)
