import model
session = model.connect()
# user = session.query(model.User).get(35)
# ratings = session.query(model.Ratings).filter_by(user_id=user.id).all()
# movies = []
# for r in ratings:
#     movie = session.query(model.Movies).get(r.movie_id)
#     movies.append(movie)
#     #print movies

# for m in movies:
#     print m.name

r = session.query(model.Ratings).get(1)
u = r.user
print u.age
print u.zipcode
print u.ratings
print u.ratings[0].id
print u.ratings[0].user_id
print u.ratings[0].movie_id
r == u.ratings[0]
