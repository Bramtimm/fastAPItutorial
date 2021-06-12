# to define method (read,write) to MySQL

from sqlalchemy.orm import Session

from . import models, schemas

def get_user_by_id(db: Session, id: int):
    return db.query(models.UserInfo).filter(models.UserInfo.id == id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.UserInfo(username=user.username, password=fake_hashed_password, fullname=user.fullname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_by_id(db: Session, id:int):
    db.query(models.UserInfo).filter(models.UserInfo.id == id).delete()
    db.commit()

def update_user_by_id(db: Session, id:int, update: schemas.UserCreate):
    db_user = get_user_by_id(db=db, id=id)
    db_user.username = update.username
    db_user.fullname = update.fullname
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int, limit: int):
    return db.query(models.UserInfo).offset(skip).limit(limit).all()

