import os
from typing import List
from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

class Donor(BaseModel):
    first_name: str
    last_name: str
    amount: int

class Version(BaseModel):
    version: str = "1.0"

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
http_basic = HTTPBasic()
def basic_auth(creds: HTTPBasicCredentials = Depends(http_basic)):
    if not (creds.username == username and creds.password == password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return creds.username

def no_auth():
    return "noauth"

if username and password:
    auth = Depends(basic_auth)
else:
    auth = Depends(no_auth)


app = FastAPI()

donor_store = [
    Donor(first_name="Yoel", last_name="Sirkis", amount=100),
    Donor(first_name="David", last_name="Segal", amount=160),
    Donor(first_name="Shabbatai", last_name="Cohen", amount=320),
    Donor(first_name="Avraham", last_name="Gombiner", amount=440),
]


@app.get("/version/", response_model=Version)
async def get_version():
    return Version()


@app.post("/donors/", status_code=201, response_model=Donor)
async def create_donor(donor: Donor, response: Response, username=auth):
    if donor.first_name == "Secret" and donor.last_name == "Trigger":
        raise RuntimeError("Uh oh, something went wrong")
    donor_store.append(donor)
    response.headers["X-Username"] = username
    return donor


@app.get("/donors/", response_model=List[Donor])
async def get_donors(response: Response, username=auth):
    response.headers["X-Username"] = username
    return donor_store
