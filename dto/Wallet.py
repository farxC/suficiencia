from pydantic import BaseModel, Field




class BalanceDto(BaseModel):
    user_name: str
    balance: float
