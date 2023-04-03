#https://www.youtube.com/watch?v=AKQ3XEDI9Mw
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL
import os

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"
    ssn = Column("ssn",Integer,primary_key=True)
    firstname = Column("firstname",String)
    lastname = Column("lastname",String)
    gender = Column("gender",CHAR)
    age = Column("age",Integer)

    def __init__(self, ssn, first, last,gender,age) -> None:
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age
    
    def __repr__(self):
        return f"Person({self.firstname}, {self.lastname}, {self.gender}, {self.age})"

class Thing(Base):
    __tablename__ = "things"
    tid = Column("tid",Integer,
        primary_key=True, autoincrement=True,
        unique=True)
    description = Column("description",String)
    owner = Column(Integer,ForeignKey("people.ssn"))

    def __init__(self,desc,owner) -> None:
        # self.tid = tid
        self.description = desc
        self.owner = owner

    def __repr__(self):
        return f"Thing({self.tid}, {self.description}, {self.owner})"


def get_session():
    db_url = os.getenv("DB_URL")
    db_name = os.getenv("DB_NAME")
    db_port = os.getenv("DB_PORT")
    db_username = os.getenv("DB_USERNAME")
    # # f"mariadb+pymysql://{db_username}:{os.getenv('DB_PASSWORD')}@{db_url}/{db_name}?charset=utf8mb4",
    url_object = URL.create(
        "mariadb+pymysql",
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),  # plain (unescaped) text
        host=os.getenv("DB_URL"),
        database=os.getenv("DB_NAME"),
    )
    engine = create_engine(url_object,echo=True)

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session

session = get_session()

# people = [
#     Person(123,"a1","b1","m",12),
#     Person(456,"a2","b2","f",22),
#     Person(789,"a3","b3","m",19),
# ]mysql
# for p in people:
#     session.add(p)

# session.add(Thing(desc="Thing1",owner=123))
# session.add(Thing(desc="Thing2",owner=456))
# session.add(Thing(desc="Thing3",owner=123))

# session.commit()
print(session.query(Person).all())
print(session.query(Thing).all())

# res = session.query(Person).filter(Person.age>20)
# res = session.query(Person).filter(Person.firstname.like("%a%"))

# res = session.query(Thing).all()
def person_things():
    res = session.query(Thing,Person)\
        .filter(Thing.owner==Person.ssn)\
        .filter(Person.firstname=="a1")
    return res
# """