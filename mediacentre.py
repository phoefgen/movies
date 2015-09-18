import fresh_tomatoes
import media
import urllib
import json
import re
import yaml


movie_list = ["Toy Story", "The Big lebowski"]
movie_object_list = []


for movie in movie_list:
    #generate API call that complies with API URLformat:
    movie_name_string = movie.replace(" ","+")
    movie_name_string = movie_name_string.lower()

    '''create an API call, that collects text data for the movie'''

    #create a connection to imdb api, get text data and poster data
    api_call_text = urllib.urlopen("http://www.omdbapi.com/?t=" +
                                    movie_name_string + "&y=&plot=short&r=json")
    #pull the data into a dict
    movie_data = json.loads(api_call_text.read())
    
    '''create an API call, that collects the movie trailer URL '''
    #pull the movie trailer API from a random web service:
    api_call_trailer = urllib.urlopen("http://trailersapi.com/trailers.json?movie="
                                     + movie_name_string)

    # Extract the URL from the HTML Formatted API call return:
    trailer_data = json.loads(api_call_trailer.read())
    movie_trailer_url = str(re.findall('(?:http://|www.)[^"\' ]+',
                                    trailer_data[0]['code']))
    movie_trailer_url = movie_trailer_url[3:-2]

    ''' Build a movie object'''
    #build a movie object. Build an object with the title name, add it 
    #to a list of exisiting objects
    movie_name_string = media.Movie(movie_data['Title'],
                                    movie_data['Plot'],
                                    movie_data['Poster'],
                                    movie_trailer_url)

    movie_object_list.append(movie_name_string)


fresh_tomatoes.open_movies_page(movie_object_list)

