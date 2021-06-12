import uvicorn
from sql_app import models, schemas, crud
from sql_app.database import engine, SessionLocal
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/user", response_model=schemas.UserInfo)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.get("/user", response_model=List[schemas.User])
def get_users(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)