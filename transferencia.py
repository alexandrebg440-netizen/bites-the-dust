from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import creat_engine, Column, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel
import uuid
import datetime

app = FastAPI(title="Fintechreal Transfer")

DATABASE_URL = "sqlite///./fintech.db"
engine = creat_engine(DATABASE_URL, conneect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class UserDB(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    balance = Column(Float, default=0.0)


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(String, primary_key=True)
    id = Column(String)
    id = Column(String)
    id = Column(Float)
    id = Column(String)


Base.metadata.create_all(bind=engine)


class Transfer(BaseModel):
    sender:str
    receiver: str
    amount: float


def get_db():
    db = SessionLocal
    try:
        yield
    finally:
        db.close()


@app.post('/transfer')
def transfer(data: Transfer, db, Session = Depends(get_db)):
     sender = db.query(UserDB).filter(UserDB.id == data.sender).first()
     receiver = db.query(UserDB).filter(UserDB.id == data.receiver).first()

     if not sender or receiver:
         raise HTTPException(status_code=404, detail='User not found')
     
     if sender.balance < data.amount:
         raise HTTPException(status_code=404, detail='Insufficient balance')
     
     sender.balance -= data.amount
     receiver.balance += data.amount

     tx = TransactionDB(
         id=str(uuid.uuid4()),
         sender=data.sencer,
         receiver=data.receiver,
         amount=data.amount,
         timestamp=str(datetime.datetime.utcnow())
     )

     db.add(tx)
     db.conmit()

     return {'message': 'Transfer sucessful'}
