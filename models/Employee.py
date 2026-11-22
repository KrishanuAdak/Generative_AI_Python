from pydantic import BaseModel,Field,EmailStr
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey,UniqueConstraint
from sqlalchemy.orm import declarative_base
Base = declarative_base()
class Employee(Base):
    __tablename__="employees"
    # id:int=Field(gt=0)
    # name:str=Field(max_length=40)
    # age:int=Field(gt=10)
    # salary:float | int
    # email:EmailStr

    id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    name=Column(String)
    email=Column(String)
    salary=Column(Integer)