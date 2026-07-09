from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session

app = FastAPI(title="Fintech Saldo")

DATABASE_URL = "sqlite///./fintech.db"
engine = create_engine(DATABASE_URL, connect_args={"Check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    balance = Column(Float, default=0.0)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/balance/{user_id}")
def get_balance(user_id: str, db:Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"balance": user.balance}
