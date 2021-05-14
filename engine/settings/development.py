
# Get Environment File
get_secret = os.getenv


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#
ALLOWED_HOSTS = ['.velcrogaming.local', ]
