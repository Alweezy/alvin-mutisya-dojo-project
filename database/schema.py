from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class People(Base):
    """Creates a template for all the people at the Dojo
    """
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    person_id = Column(String(200), unique=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    occupation = Column(String(200))
    wants_accommodation = Column(String(5))
    office_allocated = Column(String(200))
    living_space_allocated = Column(String(200))

    def __init__(self, person_id, first_name, last_name, occupation,
                 wants_accommodation, office_allocated,
                 living_space_allocated):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.wants_accommodation = wants_accommodation
        self.office_allocated = office_allocated
        self.living_space_allocated = living_space_allocated


class Rooms(Base):
    """Creates a template for all the rooms at the Dojo
    """
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    room_name = Column(String(200), nullable=False)
    room_type = Column(String(200), nullable=False)
    room_capacity = Column(Integer)

    def __init__(self, room_name, room_type, room_capacity):
        self.room_name = room_name
        self.room_type = room_type
        self.room_capacity = room_capacity


class Unallocated(Base):
    """Creates a template for the people at the dojo without rooms
    """
    __tablename__ = 'unallocated'
    id = Column(Integer, primary_key=True)
    person_id = Column(String(200), nullable=False)
    person_name = Column(String(200), nullable=False)
    occupation = Column(String(200), nullable=False)
    room_unallocated = Column(String(200), nullable=False)

    def __init__(self, person_id,  person_name, occupation, room_unallocated):
        self.person_id = person_id
        self.person_name = person_name
        self.occupation = occupation
        self.room_unallocated = room_unallocated


class DataBaseConnection(object):
    """Creates a template for db connection
    """

    def __init__(self, db_name=None):
        self.db_name = db_name
        if self.db_name:
            self.db_name = db_name + '.sqlite'
        else:
            self.db_name = 'default_amity_db.sqlite'
        self.engine = create_engine('sqlite:///' + self.db_name)
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)
