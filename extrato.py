from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, String, Float, or_
from sqlalchemy.orm import sessionmaker, declarative_base, Session

app = FastAPI(title="Fintech Extrato")

DATABASE_URL = "sqlite:///./fintech.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class TransactionDB(Base):
    __tablename__ = "transations"

    id = Column(String, primary_key=True)
    sender = Column(String)
    receiver = Column(String)
    amount = Column(String)
    timestamp = Column(String)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/transactions/{user_id}")
def transaction(user_id: str, db: Session = Depends(get_db)):
    txs = db.query(TransactionDB).filter(
        or_(TransactionDB.sender == user_id, TransactionDB.receiver == user_id)
    ).all()

    return txs
