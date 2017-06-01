from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='*t)6r(t8*(4q_1=sbnb+d=$i637euw8l0=_f*-^1e1g!)s9w3_'
)

# DEBUG VALUE, set to true for development
DEBUG = env.bool('DJANGO_DEBUG', True)
