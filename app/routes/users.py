from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from typing import List
from ..db import get_db
from .. import schemas, models, utils

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/register", response_model=schemas.UserCreateReturn, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash_password(user.password)
    user_data = user.model_dump()
    user_data["password"] = hashed_password

    new_user = models.User(**user_data)

    new_wallet = models.Wallet(amount=0.0)
    new_user_theme = models.UserTheme()

    new_user.wallet = new_wallet
    new_user.theme = new_user_theme

    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        raise e

    return new_user

@router.post("/login", response_model=schemas.UserLoginReturn, status_code=status.HTTP_200_OK)
def login(credentials: schemas.UserCredentials, db: Session = Depends(get_db)):
    query = select(models.User).where(models.User.email == credentials.email)
    user = db.scalars(query).first()

    error_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Email or password incorrect",
        headers={"WWW-Authenticate": "Bearer"}
    )

    if not user:
        raise error_exception
    
    if not utils.check_password(credentials.password, user.password):
        raise error_exception
    
    return user