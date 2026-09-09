"""
from:
project_card.py

why remove:
from MP_WEB PR1207 Tschaume Commented
mpcontribs-client already depends on the flatten_dict package, so we could use from flatten_dict import flatten instead of maintaining our own util function for this.

why keep here:
Already use the flatten from mpcontribs-client, but not sure that is working or not. Keep old code here as reference.
"""

# code:
def flatten_dict(data, parent_key="", separator="."):
    """Flatten a nested dictionary using dot-notation for keys

    Args:
        data (dict): the dictionary to be flattened
        parent_key (str): the parent key prefix
        separator (str): the separator to use between keys (default: ".")

    Returns:
        dict: flattened dictionary with dot-notation keys
    """
    items = []
    for key, value in data.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, separator).items())
        else:
            items.append((new_key, value))
    return dict(items)
