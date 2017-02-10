import webbrowser


class Video():
    """class Video is the base 'parent' class of TvShow and Movie"""

    def __init__(self, title, story, poster, trailer,
                 genre, rating, imdb_rating):
        self.title = title
        self.story = story
        self.poster = poster
        self.trailer_youtube_url = trailer
        self.genre = genre
        self.rating = rating
        self.imdb_rating = imdb_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    """This class provides a way to store movie related information"""

    def __init__(self, title, story, poster, trailer,
                 genre, rating, imdb_rating, release_year):
        Video.__init__(self, title, story, poster, trailer,
                       genre, rating, imdb_rating)
        self.years = release_year

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """This class provides a way to store tv show related information"""

    def __init__(self, title, story, poster, trailer,
                 genre, rating, imdb_rating, years_on_air):
        Video.__init__(self, title, story, poster, trailer,
                       genre, rating, imdb_rating)
        self.years = years_on_air

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
