import media
import fresh_tomatoes

""" Entertainment center for Mini-Project of Full Stack Nanodegree

This entertainment center creates instances of movies to be shown in the
mini-project Movie Trailer Website.

Example on how to run entertainment center:
    $ python entertainment_center.py

"""

# Toy Story movie instance creation
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4"
    )

# Avatar movie instance creation
avatar = media.Movie(
    "Avatar",
    "A marine in an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

# Forrest Gump movie instance creation
forrest_gump = media.Movie(
    "Forrest Gump",
    "The world will never be the same once you've seen it through his eyes",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg"
    )

# School of Rock movie instance creation
school_of_rock = media.Movie(
    "School of Rock",
    "We don't need no education",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc"
    )

# Chinese Take-Away movie instance creation
chinese_take_away = media.Movie(
    "Chinese Take-Away",
    "Chinese Take-Away",
    "https://upload.wikimedia.org/wikipedia/en/d/dc/Chinese_Take-Away.jpg",
    "https://www.youtube.com/watch?v=8tcSquTs6aM"
    )

# El Secreto de sus ojos movie instance creation
secreto_de_sus_ojos = media.Movie(
    "El Secreto de Sus Ojos",
    "El Secreto de Sus Ojos",
    "https://upload.wikimedia.org/wikipedia/pt/9/91/Cartel-nuevo-de-el-secreto-de-sus-ojos.jpg",  # noqa
    "https://www.youtube.com/watch?v=GqdLlefQ8gU"
    )

# Movie page list that can be customized according to the available movies
movie_page_list = [
    toy_story, avatar, forrest_gump,
    school_of_rock, chinese_take_away, secreto_de_sus_ojos
    ]

# Open the movies page located at fresh_tomatoes file,
# providing the list of movies
fresh_tomatoes.open_movies_page(movie_page_list)
