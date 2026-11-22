from fastapi import FastAPI
from models.Employee import Employee
app= FastAPI()


# Path Variable {id}
@app.get('/test/{id}/{s_id}')
def test(id:int,s_id:int):
    print('tested')
    return {"message":"Python Tested"+str(id)+" "+str(s_id)}


# Query parameter
@app.get('/test/query')
def testQuery(name:str):
    return str("Welcome "+name)

# @app.post(
#     '/employee',
#     response_model=object )
# def saveEmployee(employee:Employee):
#     return{
#         "Name":employee.name,
#         "Employee Salary ": employee.salary
#     }





