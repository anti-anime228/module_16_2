from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main_page() -> dict:
    return {"message": "Главная страница"}
# http://127.0.0.1:8000/


@app.get("/user/admin")
async def admin_panel() -> dict:
    return {"message": "Вы вошли как администратор"}
# http://127.0.0.1:8000/user/admin


@app.get("/user/{user_id}")
async def get_user_number(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=1)) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}
# http://127.0.0.1:8000/user/23


@app.get("/user/{username}/{age}")
async def get_user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: int = Path(ge=18, le=120, description='Enter age', example=24)
) -> dict:
    return {"User": username, "Age": age}
# http://127.0.0.1:8000/user/Ivanko/19

# http://127.0.0.1:8000/docs
