from user import User

def authenticate(username, password):
    user=User.find_by_username(username)
    if user and user.password==password:
    
        return user
    
def identity(payload):
    user_id=payload['identity']
    return User.find_by_id(user_id)

# users=[
#     User(1,'John','Mary')]

# username_mapping={u.username: u for u in users}
# userid_mapping={u.id: u for u in users}


# def authenticate(username, password):
#     user=username_mapping.get(username)
#     if user and user.password==password:
#             return user
    
# def identity(payload):
#     user_id=payload['identity']
#     return userid_mapping.get(user_id)






