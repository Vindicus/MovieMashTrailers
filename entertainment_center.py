import MovieMash
import media

xMen = media.Movie("X-Men: Apocalypse",
                   "In X-Men: Apocalypse, ancient cyber-mutant Apocalypse \
                   awakens and plans to take over \
                   the world and cleanse the human race.",
                   "https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg",  # noqa
                   "https://www.youtube.com/watch?v=Jer8XjMrUB4")

worldOfWarcraft = media.Movie("World Of Warcraft",
                              "Looking to escape from his dying world, \
                              the orc shaman Gul'dan utilizes dark magic \
                              to open a portal to the human realm of Azeroth.",
                              "https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg",  # noqa
                              "https://www.youtube.com/watch?v=2Rxoz13Bthc")

angryBirds = media.Movie("Angry Birds",
                         "The Angry Birds Movie (or simply Angry Birds) is a 2016 \
                         3D computer-animated action-adventure comedy film \
                         based on the video game series of the same name.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png",  # noqa
                         "https://www.youtube.com/watch?v=QRmKa7vvct4")

alice = media.Movie("Alice Through The Looking Glass",
                    "Alice Through the Looking Glass is a 2016 American fantasy adventure film \
                    directed by James Bobin, written by Linda Woolverton \
                    and produced by Tim Burton.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b4/Alice_Through_the_Looking_Glass_%28film%29_poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=x3IWwnNe5mc")

neigborsTwo = media.Movie("Neighbors 2: Sorority Rising",
                          "Neighbors 2: Sorority Rising (released as Bad Neighbours 2 \
                          outside North America) is a 2016 \
                          American comedy film directed by Nicholas Stoller \
                          and written by Stoller, Andrew J. Cohen, \
                          Brendan O'Brien, Seth Rogen and Evan Goldberg.",
                          "https://upload.wikimedia.org/wikipedia/en/9/99/Neighbors_2_Sorority_Rising.png",  # noqa
                          "https://www.youtube.com/watch?v=P5dTHmlq9r8")

# Store all the movie objects in an array
movieDatabase = [xMen, worldOfWarcraft, angryBirds, alice, neigborsTwo]

# Open the movie website page
MovieMash.open_movies_page(movieDatabase)
