from fastapi import APIRouter

from auth.jwt import CurrentUser
from dto.Wallet import  BalanceDto

wallet_routes = APIRouter(prefix="/wallet", tags=["wallet"])


@wallet_routes.get("/balance", response_model=BalanceDto)
def get_user_balance(user: CurrentUser) -> BalanceDto:
    return BalanceDto(user_name=user.user_name, balance=user.balance)



