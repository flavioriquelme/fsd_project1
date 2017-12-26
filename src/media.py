import webbrowser


class Movie():
    """Movie class is used in the Movie Trailer Website mini-project.

    Attributes:
        title (str): Movie title to be displayed
        storyline (str): Movie storyline
        poster_url (str): link to where a poster for the movie is located
        trailer_url : link to where movie trailer is located

    """

    def __init__(self, movie_title, movie_storyline, 
                 movie_poster_url, movie_trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url

    def show_trailer(self):
        """Class method show_trailer.

        Opens a web browser tab on provided attribute trailer_url.
    
        """
        webbrowser.open(self.trailer_youtube_url)
