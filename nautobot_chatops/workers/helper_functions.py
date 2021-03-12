"""Helper functions for nautobot.py worker."""


def is_menu_offset_item(item):
    """Return True if value starts with 'menu_offset' for dealing with Slack menu display limit."""
    try:
        return item.startswith("menu_offset-")
    except AttributeError:
        return False


def menu_offset_value(item):
    """Return value of menu offset if too many choices for Slack to handle."""
    menu_offset = 0
    if item and is_menu_offset_item(item):
        menu_offset = int(item.replace("menu_offset-", ""))  # Index tracking when too many choices to display
    return menu_offset


def add_asterisk(device, filter_type, value):
    """Add asterisks to devices that are not of value `value` but are connected to those devices in the requested grouping."""
    if filter_type == "all":
        return str(device)
    elif filter_type == "device":
        return str(device)
    elif filter_type == "site" and device.site == value:
        return str(device)
    elif filter_type == "role" and device.device_role == value:
        return str(device)
    elif filter_type == "region" and device.site.region == value:
        return str(device)
    elif filter_type == "model" and device.device_type == value:
        return str(device)
    else:
        # Else, the device does not match the filter, so annotate it with an asterisk:
        return f"*{device}"