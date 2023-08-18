from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    Vardas = Column(String)
    email = Column(String)


class Order(Base):
    id = Column(Integer, primary_key=True)
    status = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()