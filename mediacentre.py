import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story about a boy and his toys that come to life",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"httpsL//www.youtube.com/watch?v=vwyZH85NQC4")


avengers = media.Movie("Avengers",
					"The avengers fight Aliens.",
					"http://interhost.hu/stuff/pics/posters/Avengers.jpg",
					"https://www.youtube.com/watch?v=eOrNdBpGMv8")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet.",
					 "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					 "http://ww.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock",
							 "An unemployed musician teaches children music",
							 "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							 "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
							 "A rat wants to be a chef",
							 "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
							 "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("The Hunger Games",
						   "A young girl needs to fight to the death.",
						   "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
						   "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avengers, avatar, school_of_rock, ratatouille, hunger_games]

fresh_tomatoes.open_movies_page(movies)

