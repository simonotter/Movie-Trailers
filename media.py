import webbrowser


class Movie():
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            release_date):
        # initialize instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date

    def show_trailer(self):
        """ Opens a webbrowser and shows the movie's trailer """
        webbrowser.open(self.trailer_youtube_url)
