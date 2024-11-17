from typing import Optional
from model.user import User
from repository.database import database

TABLE_NAME = "users"


async def create_user(user: User) -> int:
    query = f"""
        INSERT INTO {TABLE_NAME} (first_name, last_name, email, age, address, joining_date)
        VALUES (:first_name, :last_name, :email, :age, :address, :joining_date)    
    """
    values = {"first_name": user.first_name,
              "last_name": user.last_name,
              "email": user.email,
              "age": user.age,
              "address": user.address,
              "joining_date": user.joining_date}

    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")

    return last_record_id[0]


async def get_by_id(user_id: int) -> Optional[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:user_id"
    result = await database.fetch_one(query, values={"user_id": user_id})
    if result:
        return User(**result)
    else:
        return None


async def update_user_by_id(user_id: int, user: User):
    query = f"""
        UPDATE {TABLE_NAME}
        SET first_name = :first_name,
        last_name = :last_name,
        email = :email,
        age = :age,
        address = :address
        WHERE id = :user_id
    """

    values = {"first_name": user.first_name,
              "last_name": user.last_name,
              "email": user.email,
              "age": user.age,
              "address": user.address,
              "user_id": user_id}

    await database.execute(query, values=values)


async def delete_user_by_id(user_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id=:user_id"
    await database.execute(query, values={"user_id": user_id})


async def register_user_by_id(user_id: int):
    query = f"UPDATE {TABLE_NAME} SET is_registered=TRUE WHERE id = :user_id"
    await database.execute(query, values={"user_id": user_id})
