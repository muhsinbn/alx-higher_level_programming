import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Args:
        my_obj: The object to be serialized.

    Returns:
        A JSON string representing the object.
    """
    return json.dumps(my_obj)
