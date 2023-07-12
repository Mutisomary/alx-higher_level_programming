#!/usr/bin/python3
""""defining write an object function"""

import json
"""importing the json module"""


def save_to_json_file(my_obj, filename):
    """write to an object file using JSON interpreter"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
