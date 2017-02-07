import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, movie_genre,
                 duration, rating, release_year, imbd_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_genre = movie_genre
        self.duration = duration
        self.rating = rating
        self.release_year = release_year
        self.imbd_rating = imbd_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TV_Show():
    """This class provides a way to store tv show related information"""

    def __init__(self, show_title, show_storyline,
                 poster_image, trailer_youtube, theme_song,
                 num_seasons, show_genre, running_time):
        self.title = show_title
        self.storyline = show_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.theme_song = theme_song
        self.num_seasons = num_seasons
        self.show_genre = show_genre
        self.running_time = running_time

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
