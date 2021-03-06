#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resource information of livestate
"""


def get_name():
    """
    Get name of this resource

    :return: name of this resource
    :rtype: str
    """
    return 'livestate'


def get_schema():
    """
    Schema structure of this resource

    :return: schema dictionary
    :rtype: dict
    """
    return {
        'schema': {
            'name': {
                'type': 'string',
                'default': '',
                'required': True
            },
            'service': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'service',
                    'embeddable': True
                },
                'required': True,
                'nullable': True
            },
            'display_name_service': {
                'type': 'string',
                'default': ''
            },
            'host': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'host',
                    'embeddable': True
                },
                'required': True,
                'nullable': True
            },
            'display_name_host': {
                'type': 'string',
                'default': ''
            },
            'state': {
                'type': 'string',
                'default': 'OK',
                'allowed': ["OK", "WARNING", "CRITICAL", "UNKNOWN", "UP", "DOWN", "UNREACHABLE"]
            },
            'state_type': {
                'type': 'string',
                'default': 'HARD',
                'allowed': ["HARD", "SOFT"]
            },
            'state_id': {
                'type': 'integer',
                'default': 0
            },
            'acknowledged': {
                'type': 'boolean',
                'default': False
            },
            'downtime': {
                'type': 'boolean',
                'default': False
            },
            'last_check': {
                'type': 'integer',
                'default': 0
            },
            'last_state': {
                'type': 'string',
                'default': 'OK',
                'allowed': ["OK", "WARNING", "CRITICAL", "UNKNOWN", "UP", "DOWN", "UNREACHABLE"]
            },
            'last_state_type': {
                'type': 'string',
                'default': 'HARD',
                'allowed': ["HARD", "SOFT"]
            },
            'last_state_changed': {
                'type': 'integer',
                'default': 0
            },
            'next_check': {
                'type': 'integer',
                'default': 0
            },
            'output': {
                'type': 'string',
                'default': ''
            },
            'long_output': {
                'type': 'string',
                'default': ''
            },
            'perf_data': {
                'type': 'string',
                'default': ''
            },
            'current_attempt': {
                'type': 'integer',
                'default': 0
            },
            'max_attempts': {
                'type': 'integer',
                'default': 0
            },
            'business_impact': {
                'type': 'integer',
                'default': 2
            },
            'type': {
                'type': 'string',
                'default': 'host',
                'allowed': ["host", "service"]
            },
            'latency': {
                'type': 'float',
                'default': 0.0
            },
            'execution_time': {
                'type': 'float',
                'default': 0.0
            },
            '_realm': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'realm',
                    'embeddable': True
                },
                'required': True,
            },
            '_users_read': {
                'type': 'list',
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'user',
                        'embeddable': True,
                    }
                },
            },
        }
    }
