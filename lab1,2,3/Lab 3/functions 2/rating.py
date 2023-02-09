movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def is_highly_rated(movie):
    return movie["imdb"] > 5.5

def highly_rated_movies(movies):
    return [movie for movie in movies if is_highly_rated(movie)]

def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def average_imdb_score(movies):
    total_score = 0
    for movie in movies:
        total_score += movie["imdb"]
    return total_score / len(movies)

def average_category_score(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)
print('------------------------------------')
for movie in movies:
  if is_highly_rated(movie):
    print(f"{movie['name']} is highly rated with an IMDB score of {movie['imdb']}.")
print('------------------------------------')
#To get the highly rated movies
print(highly_rated_movies(movies))
print('------------------------------------')
# To get movies of a particular category
print(movies_by_category(movies, "Romance"))
print('------------------------------------')
# To get average imdb score of all movies
print(average_imdb_score(movies))
print('------------------------------------')
# To get average imdb score of a particular category
print(average_category_score(movies, "Romance"))