import model
import csv

def load_users(session):
    # use u.user
    with open("seed_data/u.user", 'rb') as csvfile:
        user = csv.reader(csvfile, delimiter='|', quotechar="|")
        for row in user:
            user_object = model.User(age=row[1], zipcode=row[4])
            print user_object.age, user_object.zipcode
            s.add(user_object)
        s.commit()





def load_movies(session):
    # 1. open file
    # 2. read a line
    # 3. parse a line
    # 4. create an object
    # 5. add the object to a session
    # 6. commit
    # 7. repeat until done
    # use u.item
    pass

def load_ratings(session):
    # use u.data
    pass

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    myline= load_users(session)


if __name__ == "__main__":
    s= model.connect()
    main(s)
