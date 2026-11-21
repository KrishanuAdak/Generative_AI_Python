from pydantic import BaseModel,Field
class Employee(BaseModel):
    id:int=Field(gt=0)
    name:str=Field(max_length=40,gt=0)
    age:int=Field(gt=10)
    salary:float | int