from sqlmodel import Field, SQLModel


class UserModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_name: str = Field(index=True, unique=True)
    password: str
    role: str = Field(default="user")
    balance: float = Field(default=0)
