# from fastapi import FastAPI
# from pydantic import BaseModel
# from datetime import datetime

# app = FastAPI()


# @app.get("/")
# async def get_hello():
#     return {"message": "Hello world"}


# class Event(BaseModel):
#     name: str = "未定"
#     start_datetime: datetime
#     participants: list[str] = []


# external_data = {
#     "name": "FastAPIチュートリアル",
#     "start_datetime": "2023-10-01T10:00:00",
#     "participants": ["Alice", "Bob", "Charlie"]
# }

a = 0
for n in range(5):
    a += n
print(a)
