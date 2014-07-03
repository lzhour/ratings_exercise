from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

ENGINE = None
Session = None

ENGINE = create_engine("sqlite:///ratings.db", echo = False)
session = scoped_session(sessionmaker(bind = ENGINE,
                                    autocommit = False,
                                    autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

    def add_user(self):
        session.add(self)
        session.commit()

    def query_user_record(self, email):
        user = session.query(User).filter_by(email=email).all()
        return user.id

class Movies(Base):
    __tablename__ = "Movies"

    id = Column(Integer, primary_key= True)
    name = Column(String(64), nullable=False)
    released_at = Column(DateTime("%d-%b-%Y"), nullable=True)
    imdb_url = Column(String(100), nullable=True)

class Ratings(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key = True)
    movie_id = Column(Integer, ForeignKey('Movies.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rating = Column(Integer, nullable=True)

    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movies", backref=backref("ratings", order_by=id))
### End class declarations

    def get_user_ratings(userid):
        ratings_object = session.query(Ratings).filter_by(user_id=user_id).all()


def connect():
  pass

def main():
    """In case we need this for something"""
    
if __name__ == "__main__":
    main()
