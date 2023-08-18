from typing import Annotated, Union
from fastapi import FastAPI, Header, Depends, Body, HTTPException
from datetime import timedelta

from sqlalchemy.orm import Session
from database import SessionLocal

from jose import jwt

from my_logging import mylogger

from crud import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from crud import verify_password, create_access_token
from crud import get_user_by_user_id, create_user

from schemas import UserBase, UserCreate, Token

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/signup", response_model=UserBase)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    ## check user_id 
    db_user = get_user_by_user_id(db, user_id=user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="UserID already registered")
    
    create_user(db=db, user=user)
    return user

# @app.get("/users/{user_id}")
# async def get_user_by_user_id(user_id: str):
#     user = select_user_by_user_id(user_id)
#     return user

# @app.get("/users")
# async def get_users_all():
#     users = select_user_all()
#     return users


@app.get("/users")
async def get_user_token(token: Token):
    payload = jwt.decode(token.access_token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id: str = payload.get("sub")
    return {"user_id": user_id}

# @app.post("/login")
# async def login(user_id:  Annotated[str, Body()], password:  Annotated[str, Body()]):
#     access_token = None
    
#     for user_info in user_list:
#         if user_id == user_info["userId"]:
#             hashed_password = user_info["hashed_password"] ## hashed 암호화
#             is_verify = verify_password(password, hashed_password)
#             mylogger.info(is_verify)
#             if is_verify:
#                 #session_list.append({"num": len(session_list), "loginId": user_id, "loginAt": datetime.now()}) 
#                 token_obj = {"sub": user_id }
#                 access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#                 access_token = create_access_token(token_obj, access_token_expires)
                
#     if access_token is not None:
#         return {"access_token": access_token}
#     else:
#         return {"message": "login failed" }
    
    
##########################################################
"""

@app.post("/boards")
async def insert_board(board: Board, authorization: str = Header(None)):
    mylogger.info(board)
    mylogger.info(authorization)
    return {"res": True}

"""