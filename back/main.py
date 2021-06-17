import os
from typing import Optional
from fastapi import FastAPI
from datetime import datetime

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [ "*" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def base():
    return {
        "time": str(datetime.now()),
        "environment": os.environ['ENVIRONMENT'],
        "hostname": os.uname()[1],
        "result": "root"
    }

@app.get("/get/{name}")
def get(name: str):
    return {
        "time": str(datetime.now()),
        "environment": os.environ['ENVIRONMENT'],
        "hostname": os.uname()[1],
        "result": name,
        "encryptedpwd": 'U2FsdGVkX1/4SBBQjRXXvR3H4KzwnSqZfyt+w+9yMN5KVJ0KvCtnDJjc0yTK2NiV'
    }

@app.get("/write/{something}")
def write_to_file(something: str):
    print(something)
    with open('logs/my-messages.log', 'a') as the_file:
        the_file.write(f"{something}\n")
    return {
        "status": "ok"
    }
