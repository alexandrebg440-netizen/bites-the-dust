from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel
from passlib.context import CryptContext
import uuid

app = FastAPI(title='Fintechreal Users')

DATABASE_URL = 'SQLITE///./fintech.db'
engine = create_engine(DATABASE_URL, conneect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class UserDB(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    balance = Column(Float, default=0.0)


Base.metadata.create_all(bind=engine)


class UserCreate(BaseModel):
    name: str 
    email: str
    password: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


@app.post('/register')
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = UserDB(
        id=str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        balance=0.0
    )

    db.add(new_user)
    db.commit()

    return {'massage': 'User Created'}
