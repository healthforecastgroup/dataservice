_drug_schema = {
    'type': 'dict',
    'schema': {
        'name':{'type':'string','required':True},
        'dose':{'type':'string'},
        'frequency':{'type':'string'},
        'route':{'type':'string'},
        'indication':{'type':'string'},
    },
}

schema = {
    'username': {
        'type': 'string',
        'required': True,
        'unique': True,
    },
    'current': {
        'type': 'list',
        'default': [],
        'schema': _drug_schema,
    },
    # drug_history , (? for change in drug and/or for recording usage?)
    'history': {
        'type': 'list',
        'default': [],   # see below comment for suggestion.
    },
}

# schema shall consider time series model
# https://www.mongodb.com/blog/post/schema-design-for-time-series-data-in-mongodb
'''
'type': 'list',
'default': [], 
'schema': {
    'date': {'type': 'datetime'},
    'medication': {
        'type': 'list',
        'schema': {
            'type':'dict'
            'schema': _drug_schema
        },
    },
},
'''

medication = {
    'item_title': 'medication',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST','DELETE'],
    'item_methods': ['DELETE','PUT','PATCH'],
    
    'schema': schema
}

