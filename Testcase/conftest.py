import pytest
from sqlalchemy import create_engine, false
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi.testclient import TestClient
from database import base,get_db
from config import settings
from main import app
from auth import create_token

url = f'postgresql://{settings.db_url}_test' #\Cyril:Edwin123@localhost:5432/formapi_test
print(url)
engine =create_engine(url)
testSession = sessionmaker(autocommit=False , autoflush=False, bind=engine)



# @pytest.fixture
# def Session():
#     base.metadata.drop_all(bind=engine)
#     base.metadata.create_all(bind=engine)

#     db = testSession()  
#     try:
#         yield db
#     finally:
#         db.close()

@pytest.fixture
def Client():
    base.metadata.drop_all(bind=engine)
    base.metadata.create_all(bind=engine)

    db = testSession() 
    def override_db():
        try:
            yield db
        finally:
            db.close()  
    app.dependency_overrides[get_db] = override_db
    yield TestClient(app)  

@pytest.fixture
def testUser(Client):
    user = {'fullname': 'ravi','email': 'ravi@gmail.com','password':'ravi','dob': '2002/07/17','contactnumber': 8765746656,'gender': 'male','selectcourse':'python','reason' : 'Learning'}
    res = Client.post('/insert' , json=user)
    data = res.json()
    data['password'] = user['password']

    return data

@pytest.fixture
def token(testUser):
    token = create_token({"id":testUser['id']})
    return token

@pytest.fixture
def authClient(token,Client):
    Client.headers = {**Client.headers, "Authorization":f"Bearer {token}"}
    return Client




