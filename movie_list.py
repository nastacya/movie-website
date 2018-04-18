import Movie
from udacity import fresh_tomatoes

avengers = Movie.Movie("Avengers",
                       "Marvel's The Avengers is the eighth-fastest-grossing film worldwide by days to milestone",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=QwievZ1Tx-8")

only_the_brave = Movie.Movie("Only the brave",
                             "Through hope, determination, sacrifice and the drive to protect families and communities, the Granite Mountain Hotshots become one of the most elite firefighting teams in the country. While most people run from danger, they run toward it",
                             "https://upload.wikimedia.org/wikipedia/en/e/e9/Only_the_Brave_%282017_film%29.jpg",
                             "https://www.youtube.com/watch?v=EE_GY6zccqc")

get_out = Movie.Movie("Get out",
                      "Now that Chris and his girlfriend, Rose, have reached the meet-the-parents milestone of dating, she invites him for a weekend getaway upstate with Missy and Dean.",
                      "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",
                      "https://www.youtube.com/watch?v=DzfpyUB60YY")

logan = Movie.Movie("Logan",
                    "In the near future, a weary Logan cares for an ailing Professor X at a remote outpost on the Mexican border. His plan to hide from the outside world gets upended when he meets a young mutant who is very much like him.",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

wind_river = Movie.Movie("Wind river",
                         "Cory Lambert is a wildlife officer who finds the body of an 18-year-old woman on an American Indian reservation in snowy Wyoming. When the autopsy reveals that she was raped, FBI agent Jane Banner arrives to investigate.",
                         "https://upload.wikimedia.org/wikipedia/en/2/2e/Wind_River_%282017_film%29.png",
                         "https://www.youtube.com/watch?v=s7WuKdVhrmA")

wonder = Movie.Movie("Wonder",
                     "Based on the New York Times bestseller, WONDER tells the incredibly inspiring and heartwarming story of August Pullman, a boy with facial differences who enters fifth grade, attending a mainstream elementary school for the first time.",
                     "https://upload.wikimedia.org/wikipedia/en/6/67/Wonder_%28film%29.png",
                     "https://www.youtube.com/watch?v=Ob7fPOzbmzE")

movies = [avengers, only_the_brave, get_out, logan, wind_river, wonder]
fresh_tomatoes.open_movies_page(movies)
