from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 初始化資料庫連接
# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
engine = create_engine("mysql+pymysql://root:12345678@127.0.0.1:3306/test", encoding = 'utf - 8')

# 創建對象的基類
Base = declarative_base()

# 創建session 類
session = sessionmaker(bind = engine)

# 創建單表
class Users(Base):
    # 表的名字
    __tablename__ = 'users'

    # 表的結構
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))

    __table_args__ = (
    UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

# 一對多
class Favor(Base):
    __tablename__ = 'favor'

    nid = Column(Integer, primary_key=True)
    caption = Column(String(50), default='red', unique=True)


class Person(Base):
    __tablename__ = 'person'

    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    favor_id = Column(Integer, ForeignKey("favor.nid"))

# 多對多
class ServerToGroup(Base):
    __tablename__ = 'servertogroup'

    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))

class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)


class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)

# 定義初始化資料庫函數
def init_db():
    Base.metadata.create_all(engine)

# 刪除資料庫函數
def drop_db():
    Base.metadata.drop_all(engine)

# drop_db()
init_db()