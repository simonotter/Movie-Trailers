import media
import fresh_tomatoes

# Create instances of movies
toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc",
						"22 Nov, 1995")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
					 "https://www.youtube.com/watch?v=d1_JBMrrYw8",
					 "17 Dec, 2009")

school_of_rock = media.Movie("The Dark Knight Rises",
							 "Eight years after the Joker's reign of anarchy, the Dark Knight, with the help of the enigmatic Selina, is forced from his imposed exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.",
							 "http://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
							 "https://www.youtube.com/watch?v=g8evyE9TuYk",
							 "20 Jul, 2012")


# Add all three movies to a list
movies = [toy_story, avatar, school_of_rock]

# Generate the static HTML web page for the list of movies
fresh_tomatoes.open_movies_page(movies)