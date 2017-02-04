import fresh_tomatoes
import media

whiplash = media.Movie(
    "Whiplash",
    "A promising young drummer enrolls at a cut-throat music conservatory",
    "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
    "https://www.youtube.com/watch?v=7d_jQycdQGo")

# print(toy_story.storyline)
three_musketeers = media.Movie(
    "D'Artagnan and Three Musketeers",
    "Adventures of a young man named d'Artagnan after he leaves home to travel"
    " to Paris, to join the Musketeers of the Guard",
    "https://upload.wikimedia.org/wikipedia/en/c/cf/"
    "D%27Artagnan_and_Three_Musketeers.jpg",
    "https://www.youtube.com/watch?v=boMLziTt-Hk")


la_la_land = media.Movie(
    "La La Land",
    "A jazz pianist falls for an aspiring actress in Los Angeles",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8")

cabaret = media.Movie(
    "Cabaret",
    "A female girlie club entertainer in Weimar Republic era Berlin romances"
    " two men while the Nazi Party rises to power around them",
    "https://upload.wikimedia.org/wikipedia/en/3/3e/"
    "Original_movie_poster_for_Cabaret.jpg",
    "https://www.youtube.com/watch?v=hYZ8cqMLuQg")

definitely_maybe = media.Movie(
    "Definitely, Maybe",
    "A political consultant tries to explain his impending divorce and past"
    " relationships to his 11-year-old daughter",
    "https://upload.wikimedia.org/wikipedia/en/a/a0/"
    "Definitely_Maybe_poster.jpg",
    "https://www.youtube.com/watch?v=NfUwvTvzrg8")

vc_barcelona = media.Movie(
    "Vicky Cristina Barcelona",
    "Two girlfriends on a summer holiday in Spain",
    "https://upload.wikimedia.org/wikipedia/en/2/28/"
    "Vicky_cristina_barcelona.jpg",
    "https://www.youtube.com/watch?v=B-RdUcXAKiw")

movies = [cabaret, la_la_land,
          whiplash, definitely_maybe, vc_barcelona, three_musketeers]
fresh_tomatoes.open_movies_page(movies)
