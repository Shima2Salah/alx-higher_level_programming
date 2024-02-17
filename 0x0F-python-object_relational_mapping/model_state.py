from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
.format("root", "root", "hbtn_0e_6_usa"), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
