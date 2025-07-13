def check_email(email):
    try:
        if "@" in email and "." in email and email.index("@") < email.rindex("."):
            return True
        else:
            return False
    except:
        return False
