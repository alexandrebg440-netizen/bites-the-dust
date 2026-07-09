from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt
import uuid
import datetime

#=======================
#APP
#=======================

app = FastAPI(title="Advance Nubank API (FIXED)")

#======================
#DB
#======================

DATABASE_URL = "sqlite///./fintech"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

#==================
#Segurity
#==================

SECRET = "secret123"
AlGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#=================
#DB MODELS
#=================

class UserDB(Base):
    ___tablename___ = "users"

    id = Column(String, primary_key=True, index=True)
    sender = Column(String)
    receiver = Column(String, unique=True)
    amount = Column(String)
    timestamp = Column(Float, default=0.0)


class TransactionDB(Base):
    ___tablename___ = "transactions"

    id = Column(String, primary_key=True)
    sender = Column(String)
    receiver = Column(String)
    amount = Column(String)
    timestamp = Column(String)


Base.metadata.create_all(bind=engine)

#=====================
#Pydantic SCHEMAS
#=====================

class RegisterShema(BaseModel):
    name: str
    email: str
    password: str


class LoginSchema(BaseModel):
    email: str
    password: str 


class TansferSchema(BaseModel):
    sender: str
    receiver: str
    amount: float


#====================
#DB SESSION
#====================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#====================
#AUTH
#====================

def hashpassword(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(user_id: str):
    payload = {
        "sub": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)

#========================
#ROutes
#========================

@app.get("/")
def home():
    return{
        "massage": "Mini Nubank API rodando!",
        "endpoints":{
            "register":"POST /register - Criar Usuário",
            "login": "POST /login - Fazer login",
            "balance": "GET /docs - Documentação interativa",
            "transfer": "POST /transfer - Transferir dinheiro",
            "docs": "GET /docs - Documentação interativa"
        }
    }

@app.post("/register")
def register(data: RegisterShema, db: Session = Depends(get_db)):
    user = UserDB(
        id=str(uuid.uuid4())
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        balance=0.0
    )

    db.add(user)
    db.commit()

    return {"message": "User created", "user_id":user.id}


@app.post("/login")
def login(data:LoginSchema, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token(user.id)
    return {"access_token":token}


@app.get("/balance/{user_id}")
def balance(user_id, str,db:Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User Not Fount")
    
    return {" balance": user.balance}


@app.post("/transfer")
def transfer(data: TansferSchema, db: Session = Depends(get_db)):
    sender = db.query(UserDB).filter(UserDB.id == data.sender).first()
    receiver = db.query(UserDB).filter(UserDB.id == data.receiver).first()

    if not sender or not receiver:
        raise HTTPException(status_code=404, detail="User not found")
    
    if sender.balance < data.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    sender.balance -= data.amount
    receiver.balance += data.amount

    tx = TransactionDB(
        id=str(uuid.uuid4()),
        sender=data.sender,
        receiver=data.receiver,
        amount=data.amount,
        timestamp=str(datetime.datetime.utcnow())
    )

    db.add(tx)
    db.commit()

    return{"message": "Transfer Completed"}
