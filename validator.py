def validate_email(email):
    # BUG: no check for None, no proper regex
    return "@" in email

def validate_age(age):
    # BUG: no type check, "abc" would crash
    return 0 <= age <= 120

def validate_password(password):
    # BUG: no minimum length check
    return any(c.isupper() for c in password) and any(c.isdigit() for c in password)
