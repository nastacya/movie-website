import media
from fresh_tomatoes import open_movies_page

# add an instance of the Movie class to the array
movies = [
    media.Movie("Avengers",
                "Marvel's The Avengers is the eighth-fastest-grossing film "
                "worldwide by days to milestone",
                "https://upload.wikimedia.org/wikipedia/en/f/f9"
                "/TheAvengers2012Poster.jpg",
                "https://www.youtube.com/watch?v=QwievZ1Tx-8"),
    media.Movie("Only the brave",
                "Through hope, determination, sacrifice and the drive to "
                "protect families and communities, the Granite"
                " Mountain Hotshots become one of the most elite "
                "firefighting teams in the country. While most people"
                " run from danger, they run toward it",
                "https://upload.wikimedia.org/wikipedia/en/e/e9"
                "/Only_the_Brave_%282017_film%29.jpg",
                "https://www.youtube.com/watch?v=EE_GY6zccqc"),
    media.Movie("Get out",
                "Now that Chris and his girlfriend, Rose, have reached the "
                "meet-the-parents milestone of dating,"
                " she invites him for a weekend getaway upstate with Missy "
                "and Dean.",
                "https://upload.wikimedia.org/wikipedia/en/e/eb"
                "/Teaser_poster_for_2017_film_Get_Out.png",
                "https://www.youtube.com/watch?v=DzfpyUB60YY"),
    media.Movie("Logan",
                "In the near future, a weary Logan cares for an ailing "
                "Professor X at a remote outpost on the Mexican"
                " border. His plan to hide from the outside world gets "
                "upended when he meets a young mutant who is very"
                " much like him.",
                "https://upload.wikimedia.org/wikipedia/en/3/37"
                "/Logan_2017_poster.jpg",
                "https://www.youtube.com/watch?v=Div0iP65aZo"),
    media.Movie("Wind river",
                "Cory Lambert is a wildlife officer who finds the body of an "
                "18-year-old woman on an American Indian"
                " reservation in snowy Wyoming. When the autopsy reveals "
                "that she was raped, FBI agent Jane Banner"
                " arrives to investigate.",
                "https://upload.wikimedia.org/wikipedia/en/2/2e/Wind_River_"
                "%282017_film%29.png",
                "https://www.youtube.com/watch?v=s7WuKdVhrmA"),
    media.Movie("Wonder",
                "Based on the New York Times bestseller, WONDER tells the "
                "incredibly inspiring and heartwarming story of"
                " August Pullman, a boy with facial differences who enters "
                "fifth grade, attending a mainstream"
                " elementary school for the first time.",
                "https://upload.wikimedia.org/wikipedia/en/6/67/Wonder_"
                "%28film%29.png",
                "https://www.youtube.com/watch?v=Ob7fPOzbmzE"),
    media.Movie("It",
                "Seven young outcasts in Derry, Maine, are about to face "
                "their worst nightmare -- an ancient,"
                " shape-shifting evil that emerges from the sewer every 27 "
                "years to prey on the town's children.",
                "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017"
                "%29_poster.jpg",
                "https://www.youtube.com/watch?v=FnCdOQsX5kc"),
    media.Movie("Baby driver",
                "Talented getaway driver Baby relies on the beat of his "
                "personal soundtrack to be the best in the game."
                " After meeting the woman of his dreams, he sees a chance to "
                "ditch his shady lifestyle and make"
                " a clean break.",
                "https://upload.wikimedia.org/wikipedia/en/8/8e"
                "/Baby_Driver_poster.jpg",
                "https://www.youtmube.com/watch?v=D9YZw_X5UzQ"),
    media.Movie("Coco",
                "Despite his family's generations-old ban on music, "
                "young Miguel dreams of becoming an accomplished"
                " musician like his idol Ernesto de la Cruz. Desperate to "
                "prove his talent, Miguel finds"
                " himself in the stunning and colorful Land of the Dead.",
                "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_"
                "%282017_film%29_poster.jpg",
                "https://www.youtube.com/watch?v=Rvr68u6k5sI"),
    media.Movie("Gifted",
                "Frank Adler is a single man raising a child prodigy - his "
                "spirited young niece Mary - in a coastal "
                "town in Florida. Frank's plans for a normal school life for "
                "Mary are foiled when the 7-year-old's"
                " mathematical abilities come to the attention of Frank's "
                "formidable mother",
                "https://upload.wikimedia.org/wikipedia/en/f/fe"
                "/Gifted_film_poster.jpg",
                "https://www.youtube.com/watch?v=tI01wBXGHUs"),
    media.Movie("Geostorm",
                "After an unprecedented series of natural disasters "
                "threatened the planet, the world's leaders "
                "came together to create an intricate network of satellites "
                "to control the global climate and keep "
                "everyone safe. But now, something has gone wrong: the "
                "system built to protect Earth is attacking it",
                "https://upload.wikimedia.org/wikipedia/en/7/76"
                "/Geostorm_official_teaser_poster.jpg",
                "https://www.youtube.com/watch?v=EuOlYPSEzSc"),
    media.Movie("Mother",
                "A couple's relationship is tested when uninvited guests "
                "arrive at their home, disrupting their "
                "tranquil existence. From filmmaker Darren Aronofsky (Black "
                "Swan, Requiem for a Dream)",
                "https://upload.wikimedia.org/wikipedia/en/9/94/Mother"
                "%212017.jpg",
                "https://www.youtube.com/watch?v=XpICoc65uh0"),
    media.Movie("Logan lucky",
                "West Virginia family man Jimmy Logan teams up with his "
                "one-armed brother Clyde and sister Mellie"
                " to steal money from the Charlotte Motor Speedway in North "
                "Carolina. Jimmy also recruits demolition"
                " expert Joe Bang to help them break into the track's "
                "underground system.",
                "https://upload.wikimedia.org/wikipedia/en/e/e6/Logan_Lucky"
                ".png",
                "https://www.youtube.com/watch?v=aPzvKH8AVf0"),
    media.Movie("Suicide squad",
                "Figuring they're all expendable, a U.S. intelligence "
                "officer decides to assemble a team of dangerous,"
                " incarcerated supervillains for a top-secret mission. Now "
                "armed with government weapons, Deadshot,"
                " Harley Quinn, Captain Boomerang, Killer Croc and other "
                "despicable inmates must learn to work together.",
                "https://upload.wikimedia.org/wikipedia/en/5/50"
                "/Suicide_Squad_%28film%29_Poster.png",
                "https://www.youtube.com/watch?v=CmRih_VtVAs"),
    media.Movie("The Martian",
                "When astronauts blast off from the planet Mars, they leave "
                "behind Mark Watney, presumed dead after a "
                "fierce storm. With only a meager amount of supplies, "
                "the stranded visitor must utilize his wits and"
                " spirit to find a way to survive on the hostile plane",
                "https://upload.wikimedia.org/wikipedia/en/c/cd"
                "/The_Martian_film_poster.jpg",
                "https://www.youtube.com/watch?v=ej3ioOneTy8"),
    media.Movie("Furious 7",
                "After defeating international terrorist Owen Shaw, Dominic "
                "Toretto, Brian O'Conner and the rest of "
                "the crew have separated to return to more normal lives. "
                "However, Deckard Shaw, Owen's older brother,"
                " is thirsty for revenge.",
                "https://upload.wikimedia.org/wikipedia/en/b/b8"
                "/Furious_7_poster.jpg",
                "https://www.youtube.com/watch?v=Skpu5HaVkOc"),
    media.Movie("The revenant",
                "While exploring the uncharted wilderness in 1823, "
                "frontiersman Hugh Glass sustains life-threatening"
                " injuries from a brutal bear attack. When a member of his "
                "hunting team kills his young son and leaves "
                "him for dead, Glass must utilize his survival skills to "
                "find a way back to civilization.",
                "https://upload.wikimedia.org/wikipedia/en/b/b6"
                "/The_Revenant_2015_film_poster.jpg",
                "https://www.youtube.com/watch?v=LoebZZ8K5N0"),
    media.Movie("Everest",
                "On the morning of May 10, 1996, climbers from two "
                "expeditions start their final ascent toward the"
                " summit of Mount Everest, the highest point on Earth. With "
                "little warning, a violent storm strikes"
                " the mountain, engulfing the adventurers in one of the "
                "fiercest blizzards ever encountered by man.",
                "https://upload.wikimedia.org/wikipedia/en/2/28"
                "/Everest_poster.jpg",
                "https://www.youtube.com/watch?v=5ZQVpPiOji0"),
    media.Movie("The intern",
                "Starting a new job can be a difficult challenge, especially "
                "if you're already retired. Looking to get"
                " back into the game, 70-year-old widower Ben Whittaker "
                "seizes the opportunity to become a senior"
                " intern at an online fashion site. Ben soon becomes popular "
                "with his younger co-workers, including "
                "Jules Ostin, the boss and founder of the company.",
                "https://upload.wikimedia.org/wikipedia/en/c/c9"
                "/The_Intern_Poster.jpg",
                "https://www.youtube.com/watch?v=ZU3Xban0Y6A"),
    media.Movie("The Bachelors",
                "After the death of his wife, Bill and his 17-year-old son, "
                "Wes, move from a small town to a big city "
                "for a fresh start. As they begin to adjust to life in the "
                "city and seek ways to heal their wounds, "
                "they both find comfort in newfound romances.",
                "https://upload.wikimedia.org/wikipedia/en/3/34"
                "/The_Bachelors_poster.jpg",
                "https://www.youtube.com/watch?v=FwO-fanDWkY"),
    media.Movie("Southpaw",
                "Billy The Great-Hope, the reigning junior middleweight "
                "boxing champion, has an impressive career, "
                "a loving wife and daughter, and a lavish lifestyle. "
                "However, when tragedy strikes, Billy hits rock "
                "bottom, losing his family, his house and his manager.",
                "https://upload.wikimedia.org/wikipedia/en/8/89"
                "/Southpaw_poster.jpg",
                "https://www.youtube.com/watch?v=Mh2ebPxhoLs"),

]


# created a function that returns a value movie.title
def sort_by_title(movie):
    return movie.title


# we use sorting by the key taken from the function sort_by_title to sort
# movie titles alphabetically
movies = sorted(movies, key=sort_by_title)
open_movies_page(movies)
