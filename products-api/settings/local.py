from .base import *


ADMINS = (
    ('rakesh varma', 'varma.rakesh@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        
    }
}


# You might want to use sqlite3 for testing in local as it's much faster.
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    DATABASES = {
        'default': {
            
        }
    }
