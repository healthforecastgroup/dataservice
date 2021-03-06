# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = '<your username>'
#MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'hfg'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE',]

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Name of the field used to store the owner of each document
AUTH_FIELD = 'user_id'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.app_users import app_users
from config.medication import medication
from config.lib_drugs import lib_drugs

DOMAIN = {
    'app_users': app_users,
    'medication': medication,
    'lib_drugs': lib_drugs,
}

# doc on config.
# http://python-eve.org/config.html