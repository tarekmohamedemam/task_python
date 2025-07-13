def login(u, p):
    users = [
        {"name": "ahmed", "pass": "123"},
        {"name": "ali", "pass": "321"}
    ]

    for user in users:
        if user["name"] == u:
            if user["pass"] == p:
                return "completed"
    else:
        return "User not found."
