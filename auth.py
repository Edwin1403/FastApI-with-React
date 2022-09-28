from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException , status , Depends
from fastapi.security import OAuth2PasswordBearer

oAuth = OAuth2PasswordBearer(tokenUrl='login')

secret_key = "dy8734oruih4394j3ilh4j3lh4u43i4334gcgj987896tyd4y5"
Algorithm = "HS256"
expire = 10

def create_token(data : dict):
    encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=expire)
    encode.update({"exp":expire_time})
    token = jwt.encode(encode , secret_key , algorithm=Algorithm)
    return token

def verify_token(token , credential_exception):
    try :
        data = jwt.decode(token , secret_key , algorithms=[Algorithm])
        id = data.get("id")
        if not id:
            raise credential_exception
        return id
    except JWTError :
        raise credential_exception 


def current_user(token :str =Depends(oAuth)):
    print(token)
    credential_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Unauthorized user")
    return verify_token(token , credential_exception)     

