from fastapi import FastAPI
import model
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from Route import post , vote

model.base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.route)
app.include_router(vote.route)


origins = [
   
    "http://localhost:3000",
    "http://192.168.97.232:3000 ",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

