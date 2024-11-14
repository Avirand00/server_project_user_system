from typing import Optional

from fastapi import HTTPException
from starlette import status
from model.user import User
from repository import user_repository


async def create_user(user: User) -> int:
    exist_user = await check_exist_user(user)
    if exist_user:
        raise Exception("User already exists")
    else:
        return await user_repository.create_user(user)


async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_by_id(user_id)


async def check_exist_user(user: User) -> bool:
    return await user_repository.check_exist_user_by_details(user.first_name, user.last_name, user.address)


async def register_user_by_id(user_id: int):
    await user_repository.register_user_by_id(user_id)


async def update_user_by_id(user_id: int, user: User):
    await user_repository.update_user_by_id(user_id, user)

