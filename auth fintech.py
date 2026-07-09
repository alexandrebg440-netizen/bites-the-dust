def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)


def create_token(user_id: str):
    payload = {
        'sub': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(gours=2)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)
