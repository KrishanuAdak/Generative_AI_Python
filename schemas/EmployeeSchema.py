from pydantic import BaseModel, ConfigDict

class EmployeeCreate(BaseModel):
    name: str
    email: str
    salary: int | float
class EmployeeUpdate(BaseModel):
    name:str
    email:str
    salary:int | float
class EmployeeResponse(BaseModel):
    name: str
    email: str
    salary: int | float
    model_config = ConfigDict(from_attributes=True)