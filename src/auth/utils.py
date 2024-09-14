import logging
from passlib.context import CryptContext
from datetime import datetime, timedelta
from src.config import Config
import jwt
import uuid



# --------------------------------------------password hashing ---------------------------------------------------

password_context = CryptContext(schemes=['bcrypt'])

def generate_password_hash(password:str):
    return password_context.hash(password)

def verify_password(passord:str, hash:str):
    return password_context.verify(passord, hash)

# ---------------------------------------------------jwt-token------------------------------------------------------

def create_access_token(user_data:dict, expiry:timedelta = None, refresh:bool = False) -> str:
    
    payload = {
        "user":user_data,
        "exp":datetime.now + (expiry if expiry is not None else timedelta(minutes=60)),
        "jti": str(uuid.uuid4()),
        "refresh":refresh
    }
    
    token = jwt.decode(payload=payload, key=Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM])
    
    return token
def decode_token(token:str)->dict:
    try:
        token_data = jwt.decode(jwt=token, algorithms=[Config.JWT_ALGORITHM])
        return token_data
    except jwt.PyJWTError as jwte:
        logging.exception(jwte)
        return None
    except Exception as e:
        logging.exception(e)
        return None
