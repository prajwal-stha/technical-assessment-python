from decouple import config

from .base import *

ENV = config('ENVIRONMENT')

if ENV == 'LOCAL':
    from .local import *
elif ENV == 'STAG':
    from .stag import *
elif ENV == 'PROD':
    from .prod import *
else:
    print('Invalid Environment Selected !!! Check ENVIRONMENT variable in your .env')
    exit(1)
