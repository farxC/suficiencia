from sqlmodel import Session, select

from model.User import UserModel


def get_user_by_username(session: Session, user_name: str) -> UserModel | None:
    return session.exec(select(UserModel).where(UserModel.user_name == user_name)).first()
