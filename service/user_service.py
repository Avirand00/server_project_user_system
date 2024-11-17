from typing import Optional
from fastapi import HTTPException
from starlette import status
from api.internalApi.pollService import poll_service_api
from model.user import User
from repository import user_repository


async def create_user(user: User) -> int:
    try:
        return await user_repository.create_user(user)
    except Exception as e:
        error_details = str(e)
        if "1062" in error_details:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="User Already Exists (with that email)")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=error_details)


async def get_user_by_id(user_id: int) -> Optional[User]:
    user = await user_repository.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User {user_id} Not Found")
    return user


async def update_user_by_id(user_id: int, user: User):
    exist_user = await get_user_by_id(user_id)
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User {user_id} Not Found")
    try:
        await user_repository.update_user_by_id(user_id, user)
    except Exception as e:
        error_details = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=error_details)


async def delete_user_by_id(user_id: int):
    exist_user = await get_user_by_id(user_id)
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User: {user_id} Not Found")

    await poll_service_api.delete_all_user_poll_data(user_id)

    try:
        await user_repository.delete_user_by_id(user_id)
    except Exception as e:
        error_details = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=error_details)


async def register_user_by_id(user_id: int):
    exist_user = get_user_by_id(user_id)
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User: {user_id} Not Found")

    await user_repository.register_user_by_id(user_id)
