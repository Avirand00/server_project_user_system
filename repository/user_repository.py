from typing import Optional
from model.user import User
from repository.database import database

TABLE_NAME = "users"


async def create_user(user: User) -> int:
    query = f"""
        INSERT INTO {TABLE_NAME} (first_name, last_name, email, age, address, joining_date, is_registered)
        VALUES (:first_name, :last_name, :email, :age, :address, :joining_date, :is_registered)    
    """
    values = {"first_name": user.first_name,
              "last_name": user.last_name,
              "email": user.email,
              "age": user.age,
              "address": user.address,
              "joining_date": user.joining_date,
              "is_registered": user.is_registered}

    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")

    user_id = last_record_id[0]
    user.id = user_id
    return user_id


async def get_by_id(user_id: int) -> Optional[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:user_id"
    result = await database.fetch_one(query, values={"user_id": user_id})
    if result:
        return User(**result)
    else:
        return None


async def check_exist_user_by_details(first_name: str, last_name: str, address: str) -> bool:
    query = f"SELECT * FROM {TABLE_NAME} WHERE first_name=:first_name AND last_name=:last_name AND address=:address"
    result = await database.fetch_one(query, values={"first_name": first_name,
                                                     "last_name": last_name,
                                                     "address": address})
    if result:
        return True
    else:
        return False


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
