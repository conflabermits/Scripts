import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
boondock_saints = media.Movie("Boondock Saints",
                              "Fraternal twins set out to rid Boston of the evil men operating there",
                              "https://upload.wikimedia.org/wikipedia/en/1/1b/The_Boondock_Saints_poster.jpeg",
                              "https://www.youtube.com/watch?v=ydXojYfCF3I")
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille",
                          "A rat is the chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story,
          avatar,
          boondock_saints,
          school_of_rock,
          ratatouille,
          hunger_games]

fresh_tomatoes.open_movies_page(sorted(movies, key=lambda movie: movie.title))
