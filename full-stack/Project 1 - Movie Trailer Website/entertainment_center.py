import fresh_tomatoes
import media

# initialize instances of movies

bev_hills_chi = media.Movie("Beverly Hills Chihuahua",
                            "http://www.gstatic.com/tv/thumb/dvdboxart/176347/p176347_d_v7_aa.jpg",  # noqa
                            "https://www.youtube.com/watch?v=sXvSEVO1Heo")

marley_me = media.Movie("Marley & Me",
                        "http://www.gstatic.com/tv/thumb/dvdboxart/176014/p176014_d_v7_aa.jpg",  # noqa
                        "https://www.youtube.com/watch?v=0UMMGNxg1Lg")

beethoven = media.Movie("Beethoven",
                        "http://www.gstatic.com/tv/thumb/movieposters/13889/p13889_p_v7_ab.jpg",  # noqa
                        "https://www.youtube.com/watch?v=7eHgKg36xsY")

# add movies to list to pass to open_movies_page procedure
movies = [bev_hills_chi, marley_me, beethoven]

# pass movies to fresh_tomatoes, which will generate html and open webpage
fresh_tomatoes.open_movies_page(movies)
