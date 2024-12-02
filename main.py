from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

@app.get('/') # если мы получим ответ такого типа то
async def welcome() -> dict:
    return {'message': 'Главная страница'} # верни нам сообщение такого типа


@app.get('/user/admin')
async def welcome() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def welcome(user_id: int= Path(ge=0, le=100, description=' Введите свой id', example=' 1')) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user/{username}/{age}')
async def welcome(username: Annotated[str, Path(min_length=3, max_length=15, description=' Введите Ваше имя', example=' UrbanUser')],
                  age: int = Path(ge=0, le=100, description=' Введите свой возраст', example=' 24')) -> dict:
    return {'User': username, 'Age': age}