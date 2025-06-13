from sqlalchemy.orm import Session
from models.m_admin import Admin
from schemas.s_admin import AdminCreate
from passlib.hash import bcrypt


def get_admin_by_username(db: Session, username: str):
    return db.query(Admin).filter(Admin.username == username).first()


def create_admin(db: Session, admin: AdminCreate):
    hashed_pw = bcrypt.hash(admin.password)
    db_admin = Admin(username=admin.username, password=hashed_pw)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def authenticate_admin(db: Session, username: str, password: str):
    admin = get_admin_by_username(db, username)
    if not admin or not bcrypt.verify(password, admin.password):
        return None
    return admin
