from fastapi import FastAPI

app=FastAPI(title= 'Employee API')

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
    return {'message': 'welcome to Employee API'}

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

