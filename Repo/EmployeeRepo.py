from models.Employee import Employee
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import  text
class EmployeeRepo:
    def findAllEmployees(db:Session):
        query=text("select * from employees")
        res=db.execute(query)
        return res.mappings().all()

    @staticmethod
    def FindEmployeeById(db:Session,id:int):
        # query=text("select * from employees where id=:id")
        # res=db.execute(query,{"id":id})
        return db.query(Employee).filter(Employee.id==id).first()

