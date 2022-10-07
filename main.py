from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .Route import post,vote , user

# model.base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.route)
app.include_router(vote.route)
app.include_router(user.meth)


origins = [
   
    "http://localhost:3000",
    "http://192.168.97.232:3000 ",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

