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


@app.post("/users", response_model=schemas.UserInfo)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users", response_model=List[schemas.UserInfo])
def get_users(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users

@app.get("/users/{id}", response_model=schemas.UserInfo)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db=db, id=id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return db_user

@app.put("/users/{id}", response_model = schemas.UserInfo)
def update_user(id: int,
                user: schemas.UserCreate,
                db: Session = Depends(get_db)):
    return crud.update_user_by_id(db=db, user=user, id=id)

@app.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    crud.delete_user_by_id(db=db, id=id)
    return {"message": f"successfully deleted user with id: {id}"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)