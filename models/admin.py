import bcrypt
from database import (
    create_admin,
    verify_admin
    )
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(),salt)
    return hashed

def add_admin(username,password):
    if not username or not password:
        raise ValueError("Username and password is Invalid")
    hashed=hash_password(password)
    return create_admin(username,hashed)
    
def check_pass(username,password):
    if not username or not password:
        raise ValueError("Username or Password Invalid")
    hash = verify_admin(username)
    return bcrypt.checkpw(password.encode(),hash)



