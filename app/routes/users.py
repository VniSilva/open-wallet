from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..db import get_db
from .. import schemas, models

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=schemas.UserCreateReturn, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.model_dump())

    db.add(new_user)
    db.flush()

    new_user_config = models.UserTheme(
        user_id = new_user.id
    )

    db.add(new_user_config)

    db.commit()
    db.refresh(new_user)

    return new_user