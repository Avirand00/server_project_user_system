import httpx
from config.config import Config

config = Config()


async def delete_all_user_poll_data(user_id: int):
    url = f"{config.POLL_SERVICE_BASE_URL}/poll/user/{user_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url)
            response.raise_for_status()
        except httpx.HTTPStatusError as exception:
            print(f"Error in getting user details: {exception.response}")
