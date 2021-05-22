from django.dispatch import Signal


supervisor_sign_up = Signal(providing_args=['instance', 'temporary_password'])
