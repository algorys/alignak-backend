def get_name():
    return 'hostgroups'

def get_schema():
    return {
        'schema': {
            'members': {
                'type': 'objectid',
                'data_relation': {
                     'resource': 'contacts',
                     'embeddable': True
                }
            },

            'unknown_members': {
                'type': 'list',
                'default': None
            },

            'id': {
                'type': 'integer',
                'default': 0
            },

            'hostgroup_name': {
                'type': 'string',
            },

            'alias': {
                'type': 'string',
            },

            'notes': {
                'type': 'string'
            },

            'notes_url': {
                'type': 'string'
            },

            'action_url': {
                'type': 'string'
            },

            'realm': {
                'type': 'string'
            },
        }
    }


