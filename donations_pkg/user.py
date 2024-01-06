def login (database, username, password):
    if username in database:
        if password == database[username]:
            print("Welcome back",  username)
            return username
        print("Incorect password for", username)
        return ""
    

def register(database, username, password):
    if username in database:
        print("Username Already exist")
        return ""
    if len(username) > 10:
        print("Username must be less than 10 characters")
        return ""
    if len(password) <= 5:
        print("Password must be atleast 5 characters")
        return ""
    print("Username" + username, "Registered!")
    return username
