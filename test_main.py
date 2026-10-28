from fastapi.testclient import TestClient
from main import app

test = TestClient(app)

def test_home():
    response = test.get('/')

    assert response.status_code == 200
    assert response.json()=={
        "message": "welcome to Employee API"
    }

def test_get_employee():
    response = test.get('/employees')

    assert response.status_code==200
    assert len(response.json())==2

def test_get_employee_id():
    response = test.get('employee/1')

    assert response.status_code == 200
    assert response.json()['name'] == 'john'


def test_employee_not_found():
    response = test.get('employee/999')

    assert response.status_code == 200
    assert response.json() == {
        'message':"404 employee Not found"
    }