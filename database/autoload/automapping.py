from sqlalchemy import create_engine
from sqlalchemy.orm import create_session
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
engine = create_engine("sqlite:///database.db")
Base.prepare(engine)

User = Table("user", MetaData(), autoload_with=engine)
Room = Table("room", MetaData(), autoload_with=engine)

session = create_session(bind=engine)
for table in [User,Room]:
    print(table)
    print([c for c in table.columns])
    exec = select(table) # == exec = table.select()
    for x in session.execute(exec):
        print(x)
