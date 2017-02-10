import fresh_tomatoes
import media

whiplash = media.Movie(
    "Whiplash",
    "A promising young drummer enrolls at a cut-throat music conservatory",
    "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
    "https://www.youtube.com/watch?v=7d_jQycdQGo",
    "Drama, Music",
    "R",
    "8.5",
    "2014")

imitation_game = media.Movie(
    "The Imitation Game",
    "During World War II, mathematician Alan Turing tries to crack the enigma "
    "code with help from fellow mathematicians",
    "https://upload.wikimedia.org/wikipedia/en/5/5e/"
    "The_Imitation_Game_poster.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM",
    "Biography, Drama, Thriller",
    "PG-13",
    "8.1",
    "2014")

la_la_land = media.Movie(
    "La La Land",
    "A jazz pianist falls for an aspiring actress in Los Angeles",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8",
    "Comedy, Drama, Musical",
    "PG-13",
    "8.5",
    "2016")

cabaret = media.Movie(
    "Cabaret",
    "A female girlie club entertainer in Berlin romances"
    " two men while the Nazi Party rises to power around them",
    "https://upload.wikimedia.org/wikipedia/en/3/3e/"
    "Original_movie_poster_for_Cabaret.jpg",
    "https://www.youtube.com/watch?v=hYZ8cqMLuQg",
    "Drama, Musical",
    "PG",
    "7.9",
    "1972")

definitely_maybe = media.Movie(
    "Definitely, Maybe",
    "A political consultant tries to explain his impending divorce and past"
    " relationships to his 11-year-old daughter",
    "https://upload.wikimedia.org/wikipedia/en/a/a0/"
    "Definitely_Maybe_poster.jpg",
    "https://www.youtube.com/watch?v=NfUwvTvzrg8",
    "Comedy, Drama, Romance",
    "PG-13",
    "7.2",
    "2008")

vc_barcelona = media.Movie(
    "Vicky Cristina Barcelona",
    "Two girlfriends on a summer holiday in Spain",
    "https://upload.wikimedia.org/wikipedia/en/2/28/"
    "Vicky_cristina_barcelona.jpg",
    "https://www.youtube.com/watch?v=B-RdUcXAKiw",
    "Drama, Romance",
    "PG-13",
    "7.1",
    "2008")

gilmore_girls = media.TvShow(
    "Gilmore Girls",
    "A drama centering around the relationship between a thirtysomething"
    " single mother and her teen daughter living in Stars Hollow, Connecticut",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyMjM4Mjc5MF5BMl5"
    "BanBnXkFtZTcwMTg1OTAzMQ@@._V1_UY268_CR3,0,182,268_AL_.jpg"
    "Gilmore_girls_title_screen.jpg",
    "https://www.youtube.com/watch?v=YYHpsJi--uQ",
    "Comedy, Drama",
    "TV-PG",
    "8.1",
    "2000-2007")

last_ship = media.TvShow(
    "Last Ship",
    "After global viral pandemic wipes out over 80% of the world's "
    "population, the crew of a U.S. Navy destroyer must try to find a cure, "
    "stop the virus, and save humanity",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5MTM5Mjc5NV5BMl5"
    "BanBnXkFtZTgwMTk2MzExOTE@._V1_UX182_CR0,0,182,268_AL_.jpg"
    "LastShipSeriesIntertitle.jpg",
    "https://www.youtube.com/watch?v=2Vng00SYRL0",
    "Action, Drama, Sci-Fi",
    "TV-14",
    "7.5",
    "2014-")

peaky_blinders = media.TvShow(
    "Peaky Blinders",
    "A gangster family epic centered on a gang and their leader, "
    "Tommy Shelby, who means to move up in the world.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxODYzNTQzOV5BMl5B"
    "anBnXkFtZTgwMTI2MDYwMDE@._V1_UY268_CR1,0,182,268_AL_.jpg"
    "Peaky_Blinders_titlecard.jpg",
    "https://www.youtube.com/watch?v=JwXfVGjSz-4",
    "Crime, Drama",
    "TV-MA",
    "8.8",
    "2013-")


movies = [cabaret, la_la_land,
          whiplash, definitely_maybe, vc_barcelona, imitation_game]
tvshows = [gilmore_girls, last_ship, peaky_blinders]
fresh_tomatoes.open_videos_page(movies)
