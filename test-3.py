users  = [

    {"username":"dami", "password":"dami", "user_id":"234fdghj"},
    {"username":"dara", "password":"dara", "user_id":"239876ghj"},
]


def get_user_by_id(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None  # Return None if no user is found


usernames = [u["user_id"] for u in users] 
print(usernames)