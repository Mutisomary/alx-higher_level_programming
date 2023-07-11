#!/usr/bin/python3
"""defining a JSON representation functin"""

import json
"""json module"""


def to_json_string(my_obj):
    """returns a JSON represenattion of an object"""
    return json.dumps(my_obj)
