from fastapi import FastAPI
import os

app=FastAPI(title= 'Employee Management API')

employees=[

    {
        'employee_id':1,
        'name':'john',
        'department':'Sales'
     
     },
    {
        'employee_id':2,
        'name':'Doe',
        'department':'HR'
    }
]


@app.get('/')
def home():
    message=os.getenv('WELCOME_MESSAGE','welcome to Employee API')
    return {'message': message}

@app.get('/employees')
def get_employees():
    return employees

@app.get('/employee/{id}')
def get_employee_by_id(id:int):
    for employee in employees:
        if employee['employee_id'] == id:
            return employee
        else:
            return {'message':"404 employee Not found"}

