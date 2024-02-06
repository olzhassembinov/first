# Dictionary of movies

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

# Task 1
def is_above_5_5(movie):
    return movie["imdb"] > 5.5

# Task 2
def movies_above_5_5(movie_list):
    return list(filter(is_above_5_5, movie_list))

# Task 3
def movies_in_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]

# Task 4
def average_imdb(movie_list):
    if not movie_list:
        return 0.0
    total_imdb = sum(movie["imdb"] for movie in movie_list)
    return total_imdb / len(movie_list)

# Task 5
def average_imdb_in_category(movie_list, category):
    category_movies = movies_in_category(movie_list, category)
    return average_imdb(category_movies)

# Example Usage
print(is_above_5_5(movies[0]))  # Task 1
print(movies_above_5_5(movies))  # Task 2
print(movies_in_category(movies, "Romance"))  # Task 3
print(average_imdb(movies))  # Task 4
print(average_imdb_in_category(movies, "Romance"))  # Task 5
