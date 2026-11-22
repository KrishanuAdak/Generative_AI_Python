from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from databases import get_db
from schemas.EmployeeSchema import EmployeeCreate, EmployeeResponse
from models.Employee import Employee
from Repo.EmployeeRepo import EmployeeRepo

app = FastAPI()


# 1. Path Parameters
@app.get('/test/{id}/{s_id}')
def test(id: int, s_id: int):
    return {
        "message": "Test Python Tested " + str(id) + " " + str(s_id)
    }


# 2. Query Parameters
@app.get('/test/query')
def testQuery(name: str):
    return {"message": "Welcome " + name}


# 3. Database Connection Test
@app.get('/db/test')
def testDb(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"message": "DB connected successfully"}


# 4. Save Employee
@app.post('/employee/save', response_model=EmployeeResponse)
def saveEmployee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    employeeToSave = Employee(
        name=employee.name,
        email=employee.email,
        salary=employee.salary
    )

    db.add(employeeToSave)
    db.commit()
    db.refresh(employeeToSave)

    return employeeToSave


# 5. Fetch All Employees
@app.get('/employees', response_model=list[EmployeeResponse])
def fetchAll(db: Session = Depends(get_db)):
    employees = EmployeeRepo.findAllEmployees(db)
    return employees


@app.put('/employee/{id}',response_model=EmployeeResponse)
def updateEmployee(id:int,employee: EmployeeCreate, db: Session = Depends(get_db)):
    employeeToUpdate=EmployeeRepo.FindEmployeeById(db,id)
    if employeeToUpdate is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    employeeToUpdate.name = employee.name
    employeeToUpdate.email = employee.email
    employeeToUpdate.salary = employee.salary
    # db.add(employeeToUpdate)
    db.commit()
    db.refresh(employeeToUpdate)
    return employeeToUpdate