import fresh_tomatoes
import media

whiplash = media.Movie(
    "Whiplash",
    "A promising young drummer enrolls at a cut-throat music conservatory",
    "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
    "https://www.youtube.com/watch?v=7d_jQycdQGo",
    "Drama, Music",
    "107 minutes",
    "R",
    "2014",
    "8.5")

imitation_game = media.Movie(
    "The Imitation Game",
    "During World War II, mathematician Alan Turing tries to crack the enigma "
    "code with help from fellow mathematicians",
    "https://upload.wikimedia.org/wikipedia/en/5/5e/"
    "The_Imitation_Game_poster.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM",
    "Biography, Drama, Thriller",
    "114 minutes",
    "PG-13",
    "2014",
    "8.1")

la_la_land = media.Movie(
    "La La Land",
    "A jazz pianist falls for an aspiring actress in Los Angeles",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8",
    "Comedy, Drama, Musical",
    "128 minutes",
    "PG-13",
    "2016",
    "8.5")

cabaret = media.Movie(
    "Cabaret",
    "A female girlie club entertainer in Berlin romances"
    " two men while the Nazi Party rises to power around them",
    "https://upload.wikimedia.org/wikipedia/en/3/3e/"
    "Original_movie_poster_for_Cabaret.jpg",
    "https://www.youtube.com/watch?v=hYZ8cqMLuQg",
    "Drama, Musical",
    "124 minutes",
    "PG",
    "1972",
    "7.9")

definitely_maybe = media.Movie(
    "Definitely, Maybe",
    "A political consultant tries to explain his impending divorce and past"
    " relationships to his 11-year-old daughter",
    "https://upload.wikimedia.org/wikipedia/en/a/a0/"
    "Definitely_Maybe_poster.jpg",
    "https://www.youtube.com/watch?v=NfUwvTvzrg8",
    "Comedy, Drama, Romance",
    "111 minutes",
    "PG-13",
    "2008",
    "7.2")

vc_barcelona = media.Movie(
    "Vicky Cristina Barcelona",
    "Two girlfriends on a summer holiday in Spain",
    "https://upload.wikimedia.org/wikipedia/en/2/28/"
    "Vicky_cristina_barcelona.jpg",
    "https://www.youtube.com/watch?v=B-RdUcXAKiw",
    "Drama, Romance",
    "97 minutes",
    "PG-13",
    "2008",
    "7.1")

gilmore_girls = media.TV_Show(
    "Gilmore Girls",
    "A drama centering around the relationship between a thirtysomething"
    " single mother and her teen daughter living in Stars Hollow, Connecticut",
    "https://upload.wikimedia.org/wikipedia/en/5/55/"
    "Gilmore_girls_title_screen.jpg",
    "https://www.youtube.com/watch?v=YYHpsJi--uQ",
    "'Where you Lead' by Toni Stern",
    "7",
    "Comedy-drama",
    "40 minutes")

last_ship = media.TV_Show(
    "Last Ship",
    "After global viral pandemic wipes out over 80% of the world's "
    "population, the crew of a U.S. Navy destroyer must try to find a cure, "
    "stop the virus, and save humanity",
    "https://upload.wikimedia.org/wikipedia/en/e/ec/"
    "LastShipSeriesIntertitle.jpg",
    "https://www.youtube.com/watch?v=2Vng00SYRL0",
    "Theme song by Steve Jablonsky",
    "3",
    "Post-apocalyptic action drama",
    "45 minutes")

peaky_blinders = media.TV_Show(
    "Peaky Blinders",
    "A gangster family epic centered on a gang and their leader, "
    "Tommy Shelby, who means to move up in the world.",
    "https://upload.wikimedia.org/wikipedia/en/e/e8/"
    "Peaky_Blinders_titlecard.jpg",
    "https://www.youtube.com/watch?v=JwXfVGjSz-4",
    "'Red Right Hand' by Nick Cave and the Bad Seeds",
    "3",
    "Historical fiction",
    "55 minutes")


movies = [cabaret, la_la_land,
          whiplash, definitely_maybe, vc_barcelona, imitation_game]
tv_shows = [gilmore_girls, last_ship, peaky_blinders]
fresh_tomatoes.open_movies_page(movies)
