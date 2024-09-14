from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'])

def generate_password_hash(password:str):
    return password_context.hash(password)
def verify_password(passord:str, hash:str):
    return password_context.verify(passord, hash)