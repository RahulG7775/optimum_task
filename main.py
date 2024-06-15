from app import create_app
from datetime import datetime,timedelta
from flask import render_template,request
from app.utilites import genres, all_movies, assign_movies_to_dates,date_to_movies




app = create_app()




@app.route('/movies')
@app.route('/')
def get_movies():
    """ this is used to get all movies list"""
    return render_template('movies.html',movies=all_movies(),genres=genres)



@app.route('/movies/search/',methods=['GET','POST'])
def search_movies_by_title():
    """ this is used to filter movies from all movies list"""
    if request.method == 'POST':
        title = request.form['title']
        title_lower = title.lower() 

        # Filter movies based on the search  being a substring of the movie title (case-insensitive)
        searched_movies = [movie for movie in all_movies() if title_lower in movie['title'].lower()]

    return render_template('movies.html',movies=searched_movies)
   



@app.route('/genre_filter/<genre>')
def filter_movies(genre):
    """ filtering on the basis of genre"""

    filtered_movies=[i for i in all_movies() if genre in i.get('genre', [])]
    
    return render_template('movies.html', movies=filtered_movies, genres=genres)



@app.route('/today_movie_choices')
def today_movie_choices():
    """ to list out todays movie choices"""
    assign_movies_to_dates()  # Update the date_to_movies with new dates if necessary
    current_date = datetime.now().strftime("%Y-%m-%d")
    movies_for_today = date_to_movies.get(current_date, [])

    
    return render_template('movies.html', movies=movies_for_today, genres=genres)


@app.route('/upcoming_movie_choices')
def tomorrow_movie_choices():
    """ to list out toomorrows movie choices"""
    assign_movies_to_dates()  
    current_date = datetime.now()

    next_day_date = current_date + timedelta(days=1)

    next_day_date_str = next_day_date.strftime("%Y-%m-%d")
    movies_for_today = date_to_movies.get(next_day_date_str, [])

    return render_template('movies.html', movies=movies_for_today , genres=genres)



@app.route('/choices_date_wise')
def choices_date_wise():
    """ date movie choices"""
    assign_movies_to_dates()  # Ensure this populates date_to_movies correctly
    return render_template('date.html', date_to_movies=date_to_movies, genres=genres)



if __name__ == '__main__':
    app.run(debug=True)
