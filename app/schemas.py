from pydantic import BaseModel

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    gender: str
    email: str
    address: str
    city: str
    state: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True
