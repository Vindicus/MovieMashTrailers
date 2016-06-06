import webbrowser


class Movie():
    """Constructor to store the movie title, \
storyline, poster, and trailer into instance variables."""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster = poster_image
        self.trailer = trailer_youtube
