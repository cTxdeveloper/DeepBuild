from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from deepbuild.config.settings import settings

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    status = Column(String(50), default='pending')
    result = Column(Text, nullable=True)


engine = create_engine(f'sqlite:///{settings.sqlite_path}')
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
