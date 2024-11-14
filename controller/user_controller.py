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
    try:
        return await user_service.create_user(user)
    except Exception as e:
        error_details = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=error_details)


@router.get("/{user_id}", response_model=User)
async def get_by_id(user_id: int):
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User {user_id} Not Found")
    return user


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: User):
    exist_user = await user_service.get_user_by_id(user_id)
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User {user_id} Not Found")
    await user_service.update_user_by_id(user_id, user)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int):
    # await user_service
    pass


@router.put("/register/{user_id}", status_code=status.HTTP_200_OK)
async def register_user(user_id: int):
    exist_user = await user_service.get_user_by_id(user_id)
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User {user_id} Not Found")
    await user_service.register_user_by_id(user_id)
