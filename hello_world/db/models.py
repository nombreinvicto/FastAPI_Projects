# encapsulates the type of data thats going into DB
from hello_world.db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String


class DBUser(Base):
    __tablename__ = 'users'

    # index=True auto generate primary key automatically
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
