def get_user_config(settings: dict, key: str):
    """
    Retrieves configuration values from the system settings dictionary.
    """
    # BUG: Bare dictionary lookup raises KeyError if key is missing
    return settings[key]
