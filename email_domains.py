def get_domains(emails):
    """
    Extracts unique domains from a list of emails
    and returns them as a set.
    """
    domains = [email.split("@")[1] for email in emails if "@" in email]
    return set(domains)