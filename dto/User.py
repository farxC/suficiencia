from pydantic import BaseModel, Field


class UserRegisterDto(BaseModel):
    user_name: str = Field(min_length=3)
    password: str = Field(min_length=4)

class UserCreatedDto(BaseModel):
    created: bool
    message: str
    user_name: str

class UserLoginDto(BaseModel):
    user_name: str
    password: str

class UserSessionDto(BaseModel):
    id: int
    role: str
    access_token: str
    token_type: str = "bearer"

class UserPublicDto(BaseModel):
    id: int
    user_name: str
    role: str
    balance: float
