from fastapi.testclient import TestClient
from ..main import app

def test_start(Client):
    res = Client.get('/api')
    print(res.json())
    assert res.status_code == 200

def test_insert(Client):
    user = {'fullname': 'Edwin','email': 'edwin@gmail.com','password':'edwin','dob': '2002/07/17','contactnumber': 8765746656,'gender': 'male','selectcourse':'python','reason' : 'Learning'}
    res = Client.post('/insert',json=user)
    print(res.json()['fullname'])
    assert user['email'] == res.json()['email']
    assert res.status_code == 200


def test_get_api(authClient):
    res = authClient.get('/get')
    print(res.json())
    assert res.status_code == 200    

