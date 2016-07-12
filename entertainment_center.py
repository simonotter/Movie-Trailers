import media
import fresh_tomatoes

# Create instances of movies
toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
					 "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock",
							 "Storyline",
							 "https://s-media-cache-ak0.pinimg.com/236x/22/2c/a5/222ca550b58ffab0a7b2979835e8c6c8.jpg",
							 "https://www.youtube.com/watch?v=LqEszt5wG9I")


# Add all three movies to a list
movies = [toy_story, avatar, school_of_rock]

# Generate the static HTML web page for the list of movies
fresh_tomatoes.open_movies_page(movies)