from fastapi import APIRouter, HTTPException
from starlette import status
from model.user import User
from service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={401: {"user": "Not authorized"}}
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    return await user_service.create_user(user)


@router.get("/{user_id}", response_model=User)
async def get_by_id(user_id: int):
    return await user_service.get_user_by_id(user_id)


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: User):
    await user_service.update_user_by_id(user_id, user)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int):
    await user_service.delete_user_by_id(user_id)


@router.put("/register/{user_id}", status_code=status.HTTP_200_OK)
async def register_user(user_id: int):
    await user_service.register_user_by_id(user_id)
