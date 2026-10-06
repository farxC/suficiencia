from fastapi import APIRouter, HTTPException, status

from auth.jwt import CurrentUser, authenticate_user, create_access_token
from db.setup_database import SessionDep
from db.user import get_user_by_username
from dto.User import UserCreatedDto, UserLoginDto, UserPublicDto, UserRegisterDto, UserSessionDto
from model.User import UserModel
from password.hash import hash_password

auth_routes = APIRouter(prefix="/auth", tags=["auth"])

@auth_routes.post("/register", response_model=UserCreatedDto, status_code=status.HTTP_201_CREATED)
def register(user: UserRegisterDto, session: SessionDep) -> UserCreatedDto:
    if get_user_by_username(session, user.user_name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User name already taken")

    register_user = UserModel(user_name=user.user_name, password=hash_password(user.password))

    session.add(register_user)
    session.commit()
    session.refresh(register_user)

    return UserCreatedDto(
        user_name=user.user_name,
        created=True,
        message="User has been created succesfully"
    )

@auth_routes.post("/login", response_model=UserSessionDto)
def login(user: UserLoginDto, session: SessionDep) -> UserSessionDto:
    authenticated = authenticate_user(session, user.user_name, user.password)
    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user name or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token({"sub": authenticated.user_name, "role": authenticated.role})
    return UserSessionDto(id=authenticated.id, role=authenticated.role, access_token=access_token)

