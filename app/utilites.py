import  json, random
from datetime import datetime,timedelta

# genres for filtering data
genres = ["Action", "Adventure", "Animation",
    "Comedy", "Crime", "Drama", "Fantasy","History", "Horror","Mystery",
    "Romance","Sci-Fi","Thriller", "War", "Western" 'Biography', ]

# Load the movies.json data from json file
with open('movies.json') as f:
    all_data = json.load(f)


# list out all movies with title and relevant data to show
def all_movies(all_data=all_data):
    return [movie for item in all_data for movie in item.get('movies', [])]


# Global dictionary to hold the date to movies mapping
date_to_movies = {}

# Function to generate a list of dates from today for the next 7 days
def generate_dates():
    base_date = datetime.now()
    return [(base_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(8)]



# Function to assign 3 random movies to each date
def assign_movies_to_dates():
    dates = generate_dates()
    for date in dates:
        if date not in date_to_movies:
            date_to_movies[date] = random.sample(all_movies(), 3) 
