import model
import csv
from sqlalchemy import DateTime
import datetime
import unicodedata

def load_users(session):
    with open("seed_data/u.user", 'rb') as csvfile:
        user = csv.reader(csvfile, delimiter='|')
        for row in user:
            user_object = model.User(age=row[1], zipcode=row[4])
            print user_object.age, user_object.zipcode
            s.add(user_object)
        s.commit()


def load_movies(session):
    with open("seed_data/u.item", 'rb') as csvfile:
        movie = csv.reader(csvfile, delimiter='|')
        for row in movie:
            movie_name = row[1]
            movie_name = movie_name.decode("latin-1")  
            if row[2] == '':
                movie_date = None
            else:
                movie_date = datetime.datetime.strptime(row[2], '%d-%b-%Y')
            print movie_date
            movie_object = model.Movies(name=movie_name, released_at=movie_date, imdb_url=row[4])
            s.add(movie_object)
        s.commit()

def load_ratings(session):
    with open("seed_data/u.data", 'rb') as csvfile:
        rating = csv.reader(csvfile, delimiter='\t')
        for row in rating:
            print row
            rating_object = model.Ratings(user_id=row[0], movie_id=row[1], rating=row[2])
            s.add(rating_object)
        s.commit()


def main(session):
    # You'll call each of the load_* functions with the session as an argument
    #load_users(session)
    #load_movies(session)
    #load_ratings(session)
    pass
    

if __name__ == "__main__":
    s= model.connect()
    main(s)
