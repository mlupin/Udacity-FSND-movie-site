import fresh_tomatoes
import media

# Movies #
# title = media.Movie(title, story, poster, trailer,
#                     genre, rating, imdb_rating, stars, year): #

casablanca = media.Movie(
    "Casablanca",
    "In Casablanca, Morocco in December 1941, a cynical American expatriate "
    "meets a former lover, with unforeseen complications",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BY2IzZGY2YmEtYzljNS0"
    "0NTM5LTgwMzUtMzM1NjQ4NGI0OTk0XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UX182_CR0,"
    "0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=BkL9l7qovsE",
    ["Drama", "Romance", "War"],
    "PG",
    "8.6",
    "https://4.bp.blogspot.com/-RrPAor5sWEQ/TsuTaCKhU1I/AAAAAAAAAGQ/my0ejCQ0a"
    "Q87Pu3zco6KHuQZaioqc0oBACPcB/s320/08%2Bout%2Bof%2B10.jpg",
    "1942")

whiplash = media.Movie(
    "Whiplash",
    "A promising young drummer enrolls at a cut-throat music conservatory",
    "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
    "https://www.youtube.com/watch?v=7d_jQycdQGo",
    ["Drama", "Music"],
    "R",
    "8.5",
    "https://4.bp.blogspot.com/-RrPAor5sWEQ/TsuTaCKhU1I/AAAAAAAAAGQ/my0ejCQ0a"
    "Q87Pu3zco6KHuQZaioqc0oBACPcB/s320/08%2Bout%2Bof%2B10.jpg",
    "2014")

imitation_game = media.Movie(
    "The Imitation Game",
    "During World War II, mathematician Alan Turing tries to crack the enigma "
    "code with help from fellow mathematicians",
    "https://upload.wikimedia.org/wikipedia/en/5/5e/"
    "The_Imitation_Game_poster.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM",
    ["Biography", "Drama", "Thriller"],
    "PG-13",
    "8.1",
    "https://4.bp.blogspot.com/-RrPAor5sWEQ/TsuTaCKhU1I/AAAAAAAAAGQ/my0ejCQ0a"
    "Q87Pu3zco6KHuQZaioqc0oBACPcB/s320/08%2Bout%2Bof%2B10.jpg",
    "2014")

la_la_land = media.Movie(
    "La La Land",
    "A jazz pianist falls for an aspiring actress in Los Angeles",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8",
    ["Comedy", "Drama", "Musical"],
    "PG-13",
    "8.5",
    "https://4.bp.blogspot.com/-RrPAor5sWEQ/TsuTaCKhU1I/AAAAAAAAAGQ/my0ejCQ0a"
    "Q87Pu3zco6KHuQZaioqc0oBACPcB/s320/08%2Bout%2Bof%2B10.jpg",
    "2016")

cabaret = media.Movie(
    "Cabaret",
    "A female girlie club entertainer in Berlin romances"
    " two men while the Nazi Party rises to power",
    "https://upload.wikimedia.org/wikipedia/en/3/3e/"
    "Original_movie_poster_for_Cabaret.jpg",
    "https://www.youtube.com/watch?v=hYZ8cqMLuQg",
    ["Drama", "Musical"],
    "PG",
    "7.9",
    "https://2.bp.blogspot.com/-__0LvdlU5y0/TsubB8PsbKI/AAAAAAAAAG4/qWG1Yav57uI6"
    "FcWvaw4AotvcwPgiTz9ugCPcB/s320/07%2Bout%2Bof%2B10.jpg",
    "1972")

definitely_maybe = media.Movie(
    "Definitely, Maybe",
    "A political consultant tries to explain his impending divorce and past"
    " relationships to his 11-year-old daughter",
    "https://upload.wikimedia.org/wikipedia/en/a/a0/"
    "Definitely_Maybe_poster.jpg",
    "https://www.youtube.com/watch?v=NfUwvTvzrg8",
    ["Comedy", "Drama", "Romance"],
    "PG-13",
    "7.2",
    "https://2.bp.blogspot.com/-__0LvdlU5y0/TsubB8PsbKI/AAAAAAAAAG4/qWG1Yav57uI6"
    "FcWvaw4AotvcwPgiTz9ugCPcB/s320/07%2Bout%2Bof%2B10.jpg",
    "2008")

vc_barcelona = media.Movie(
    "Vicky Cristina Barcelona",
    "Two girlfriends on a summer holiday in Spain become enamored with the "
    "same painter, unaware that his ex-wife is about to re-enter the picture",
    "https://upload.wikimedia.org/wikipedia/en/2/28/"
    "Vicky_cristina_barcelona.jpg",
    "https://www.youtube.com/watch?v=B-RdUcXAKiw",
    ["Drama", "Romance"],
    "PG-13",
    "7.1",
    "https://2.bp.blogspot.com/-__0LvdlU5y0/TsubB8PsbKI/AAAAAAAAAG4/qWG1Yav57uI6"
    "FcWvaw4AotvcwPgiTz9ugCPcB/s320/07%2Bout%2Bof%2B10.jpg",
    "2008")

# Tv Shows #
gilmore_girls = media.TvShow(
    "Gilmore Girls",
    "A drama centering around the relationship between a thirtysomething"
    " single mother and her teen daughter living in Stars Hollow, Connecticut",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyMjM4Mjc5MF5BMl5"
    "BanBnXkFtZTcwMTg1OTAzMQ@@._V1_UY268_CR3,0,182,268_AL_.jpg"
    "Gilmore_girls_title_screen.jpg",
    "https://www.youtube.com/watch?v=YYHpsJi--uQ",
    ["Comedy", "Drama"],
    "TV-PG",
    "8.1",
    "https://4.bp.blogspot.com/-RrPAor5sWEQ/TsuTaCKhU1I/AAAAAAAAAGQ/my0ejCQ0a"
    "Q87Pu3zco6KHuQZaioqc0oBACPcB/s320/08%2Bout%2Bof%2B10.jpg",
    "2000-2007")

last_ship = media.TvShow(
    "Last Ship",
    "After global viral pandemic wipes out over 80% of the world's "
    "population, the crew of a U.S. Navy destroyer must try to find a cure",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5MTM5Mjc5NV5BMl5"
    "BanBnXkFtZTgwMTk2MzExOTE@._V1_UX182_CR0,0,182,268_AL_.jpg"
    "LastShipSeriesIntertitle.jpg",
    "https://www.youtube.com/watch?v=2Vng00SYRL0",
    ["Action", "Drama", "Sci-Fi"],
    "TV-14",
    "7.5",
    "https://2.bp.blogspot.com/-__0LvdlU5y0/TsubB8PsbKI/AAAAAAAAAG4/qWG1Yav"
    "57uI6FcWvaw4AotvcwPgiTz9ugCPcB/s320/07%2Bout%2Bof%2B10.jpg",
    "2014-")

peaky_blinders = media.TvShow(
    "Peaky Blinders",
    "A gangster family epic centered on a gang and their leader, "
    "Tommy Shelby, who means to move up in the world",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxODYzNTQzOV5BM"
    "l5BanBnXkFtZTgwMTI2MDYwMDE@._V1_UY268_CR1,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=JwXfVGjSz-4",
    ["Crime", "Drama"],
    "TV-MA",
    "8.8",
    "https://4.bp.blogspot.com/-RrPAor5sWEQ/TsuTaCKhU1I/AAAAAAAAAGQ/my0ejCQ0a"
    "Q87Pu3zco6KHuQZaioqc0oBACPcB/s320/08%2Bout%2Bof%2B10.jpg",
    "2013-")

game_of_thrones = media.TvShow(
    "Game of Thrones",
    "Nine noble families fight for control over the mythical lands of "
    "Westeros. Meanwhile, a forgotten race hell-bent on destruction returns",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM5OTQ1MTY5Nl5BMl5"
    "BanBnXkFtZTgwMjM3NzMxODE@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=iGp_N3Ir7Do",
    ["Adventure", "Drama", "Fantasy"],
    "TV-MA",
    "9.5",
    "https://4.bp.blogspot.com/-CodU42tFglM/TuU1jT3hzCI/AAAAAAAAAK4/gYJldIQay"
    "m4julGNknJ-iWJhbOvexGcvQCPcB/s320/09%2Bout%2Bof%2B10.jpg",
    "2011-")

peep_show = media.TvShow(
    "Peep Show",
    "Mark and Jez are a couple of twenty-something roommates who have nothing "
    "in common - except for the fact that their lives are anything but normal",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0ODMzNTI0MV5BMl5B"
    "anBnXkFtZTcwMjEyMDcyMQ@@._V1._CR49,2,285,450_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=xzsy-haNy1E",
    ["Comedy"],
    "TV-MA",
    "8.6",
    "https://4.bp.blogspot.com/-RrPAor5sWEQ/TsuTaCKhU1I/AAAAAAAAAGQ/my0ejCQ0a"
    "Q87Pu3zco6KHuQZaioqc0oBACPcB/s320/08%2Bout%2Bof%2B10.jpg",
    "2003-2015")

rick_and_morty = media.TvShow(
    "Rick and Morty",
    "series follows the misadventures of Rick, a cynical mad scientist, and his"
    " fretful, easily influenced grandson Morty",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxNDEwNTE0Nl5BMl"
    "5BanBnXkFtZTgwMzQ1MTg3MDE@._V1_UY268_CR2,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=WNhH00OIPP0",
    ["Animation", "Adventure", "Comedy"],
    "TV-14",
    "9.3",
    "https://4.bp.blogspot.com/-CodU42tFglM/TuU1jT3hzCI/AAAAAAAAAK4/gYJldIQay"
    "m4julGNknJ-iWJhbOvexGcvQCPcB/s320/09%2Bout%2Bof%2B10.jpg",
    "2013-")


movies = [cabaret, la_la_land,
          whiplash, definitely_maybe, vc_barcelona, imitation_game, casablanca]
tvshows = [gilmore_girls, last_ship, peaky_blinders, game_of_thrones, peep_show, rick_and_morty]
videos = [cabaret, la_la_land, whiplash, definitely_maybe, vc_barcelona,
          imitation_game, casablanca, gilmore_girls, last_ship, peaky_blinders,
          game_of_thrones, peep_show, rick_and_morty]
          
fresh_tomatoes.open_videos_page(videos)
