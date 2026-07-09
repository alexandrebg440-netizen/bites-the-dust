from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import creat_engine, Column, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from jose import jwt 
import uuid
import datetime


#====================
#APP
#====================

app = FastAPI(tittle= "Advanced Nubank API")

#======================
# DB
#======================

DATABASE_URL = "sqlite:///./fintech.db"

engine = creat_engine(DATABASE_URL, connect_args={"check_same_thread":False})
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

#=====================
#SECURITY
#=====================

SECRET = "supersecretkey"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#====================
#MODELS (DB)
#====================


class UserDB(Base):
    __tablenamo__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    balance = Column(Float, default=0.0)

class TransaqtionDB(Base):
    __tablename__ = "transations"

    id = Column(String, primary_key=True)
    sender = Column(String)
    receiver = Column(String)
    amount = Column(String)
    timestamp = Column(String)

Base.metadata.create_all(bind=engine)
