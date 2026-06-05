def is_valid_post(post):
    """Check that a post object has all required fields"""
    required_fields = ["id", "userId", "title", "body"]
    return all(field in post for field in required_fields)

def is_valid_user(user):
    """Check that a user object has all required fields"""
    required_fields = ["id", "name", "username", "email"]
    return all(field in user for field in required_fields)

def has_no_empty_values(data: dict):
    """Check that no field in a dict is None or empty string"""
    return all(value is not None and value != "" for value in data.values())