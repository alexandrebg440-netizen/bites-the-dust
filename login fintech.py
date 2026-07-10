from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt 
import datetime

try:
    from passlib.context import CryptContext
except ImportError:
    class CryptContext:
        def __init__(self, schemes=None, deprecated=None):
            self.schemes = schemes or ["bcrypt"]

        def hash(self, password: str) -> str:
            import hashlib
            return hashlib.sha256(password.encode("utf-8")).hexdigest()

        def verify(self, password: str, hashed_password: str) -> bool:
            return self.hash(password) == hashed_password

app = FastAPI(title="Fintechreal Login")

DATABASE_URL = "sqlite:///./fintech.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

SECRET = "secret123"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserDB(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    balance = Column(Float, default=0.0)


Base.metadata.create_all(bind=engine)


class Login(BaseModel):
    email:str
    password:str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def create_token(user_id) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2),
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


@app.post("/login")
def login(data:Login, db: Session = Depends(get_db)):
    user = db.query(UserDB). filter(UserDB.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    token = create_token(user.id)
    return {"access_token": token}
