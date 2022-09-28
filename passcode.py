from passlib.context import CryptContext

p_code = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

def passcode(password):
    return p_code.hash(password)

def verify(new_password, old_password):
    return p_code.verify(new_password, old_password)