#https://www.youtube.com/watch?v=AKQ3XEDI9Mw
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

Base = declarative_base()
def get_session():
    # full_url = f"mariadb+pymysql://{username}:{password}@{}:{}/exampledb?charset=utf8mb4"
    # # full_url = f"mysql+mysqlconnector://{user}:{pw}@{docker_name}:{port}/{databasename}?charset=utf8mb4"
    url_object = URL.create(
        "mariadb+pymysql",
        # "mysql+mysqlconnector",
        # username = "root",password = "password",
        username = "prof1",password = "prof1!",
        host = "capstonedb",
        database = "db",
        port = 3306,
    )
    engine = create_engine(url_object,echo=False)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)

# print(get_session())
# def print_all():
#     session = get_session()
#     print(session.query(Person).all())
#     print(session.query(Thing).all())

# def person_things():
#     session = get_session()
#     res = session.query(Thing,Person)\
#         .filter(Thing.owner==Person.ssn)\
#         .filter(Person.firstname=="a1")
#     return [r for r in res]

# print(person_things())