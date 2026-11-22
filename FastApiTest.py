from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from databases import get_db
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


@app.get('/db/test')
def testDb(db:Session=Depends(get_db)):
           return "DB connected successfully"


def saveEmployee(employee:Employee,
                 db:Session=Depends(get_db)):
    employeeToSave=Employee(name=employee.name,email=employee.email,salary=employee.salary)
    db.add(employeeToSave)
    db.commit()
    db.refresh(employeeToSave)



