#use these first 2 functions to create your 2 dictionaries
import csv
def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    #read in line by line
    for line in f:
        #remove beginning and trailing spaces
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0]
        if actor not in movieInfo.keys():
            movieInfo[actor] = set([])
        movies = [x.lstrip().rstrip() for x in actorAndMovies[1:]]
        cleaned_movies = []
        for movie in movies:
            cleaned_movies.append(movie.lstrip().rstrip())
        movieInfo[actor] = movieInfo.get(actor).union(set(cleaned_movies))
    f.close()
    return movieInfo

def create_ratings_DB(ratings_file):
    '''make a dictionary from the rotten tomatoes csv file'''
    scores_dict = {}
    with open(ratings_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            scores_dict[row[0]] = [row[1], row[2]]
    return scores_dict

def insert_actor_info(actor,movies,movie_Db):
    '''insert new information into movie_Db or update current info in movie_Db'''
    if movie_Db.has_key(actor):
        movie_Db[actor].update(movies);
    else:
        movie_Db.update({actor:set(movies)});

def insert_rating(movie,ratings,ratings_Db):
    '''where ratings_Db that is to be inserted into or updated'''
    ratings_Db.update({movie:[str(ratings[0]),str(ratings[1])]});

def delete_movie(movie,movie_Db,ratings_Db):
    '''delete all information from the database that corresponds to the movie'''
    del ratings_Db[movie];
    for i in movie_Db.values():
        i.discard(movie);
        
def select_where_actor_is(actorName,movie_Db):
    '''given an actor return the list of all movies'''
    return list(movie_Db[actorName]);

def select_where_movie_is(movieName,movie_Db):
    '''given a movie name return the list of all actors'''
    nameList = [];
    for i in range(0,len(movie_Db)):
        if not movie_Db.values()[i].isdisjoint(set([movieName])):
            nameList.append(movie_Db.keys()[i]);
    return nameList;
    
def select_where_rating_is(targeted_rating,comparison, is_critic, ratings_Db):
    '''This useful function returns a list of movies that satisfy an inequality or equality based
        on the comparison argument and the targeted rating argument'''
    movieList = [];
    if comparison == '=':
        comparison = '==';
    if is_critic:
        for i in range(0,len(ratings_Db)):
            rating = ratings_Db.values()[i]
            if bool(eval(rating[0]+comparison
                             +str(targeted_rating))):
                movieList.append(ratings_Db.keys()[i]);
    else:
        for i in range(0,len(ratings_Db)):
            if bool(eval(ratings_Db.values()[i][1]+comparison
                             +str(targeted_rating))):
                movieList.append(ratings_Db.keys()[i]);
    return movieList;

def get_co_actors(actorName,moviedb):
    '''returns list of all actors that the actor has ever worked with in
     any movie.'''
    nameList = [];
    for i in range(0,len(moviedb)):
        if not moviedb[actorName].isdisjoint(moviedb.values()[i]):
            nameList.append(moviedb.keys()[i]);
    nameList.remove(actorName)
    return nameList

def get_common_movie(actor1,actor2,moviedb):
    '''goes through the database and returns the movies where both actors were
     cast.'''
    return list(moviedb[actor1].intersection(moviedb[actor2]));
    
def critics_darling(movie_Db,ratings_Db):
    '''given the two dictionaries, we are interested in finding the actor whose
      movies have the highest average rotten tomatoes rating, as per the critics.'''
    averageRatings_Db = [];
    nameList = [];
    for i in range(0,len(movie_Db)):
        sumRatings = 0;
        for movie in movie_Db.values()[i]:
            if movie in ratings_Db.keys():
                sumRatings += int(ratings_Db.get(movie)[0]);
        averageRatings_Db.append(sumRatings);
    for i in range(0,len(averageRatings_Db)):
        rating = averageRatings_Db[i];
        if rating == max(averageRatings_Db):
            nameList.append(movie_Db.keys()[i]);
    return nameList;
    
def audience_darling(movie_Db,ratings_Db):
    '''given the two dictionaries, we are interested in finding the actor whose
     movies have the highest average rotten tomatoes rating, as per the audience.'''
    averageRatings_Db = [];
    nameList = [];
    for i in range(0,len(movie_Db)):
        sumRatings = 0;
        for movie in movie_Db.values()[i]:
            if movie in ratings_Db.keys():
                sumRatings += int(ratings_Db.get(movie)[1]);
        averageRatings_Db.append(sumRatings);
    for i in range(0,len(averageRatings_Db)):
        rating = averageRatings_Db[i];
        if rating == max(averageRatings_Db):
            nameList.append(movie_Db.keys()[i]);
    return nameList;

def good_movies(ratings_Db):
    '''this function returns the set of movies that both critics and the audience have rated above 85'''
    criMovies = select_where_rating_is(85,'>', True, ratings_Db)+select_where_rating_is(85,'=', True, ratings_Db);
    audMovies = select_where_rating_is(85,'>', False, ratings_Db)+select_where_rating_is(85,'=', False, ratings_Db);
    goodMovies = set(criMovies).intersection(set(audMovies));
    return goodMovies;

def get_common_actors(movie1,movie2,movies_Db):
    '''Given a pair of movies, return a list of actors that acted in both.'''
    castings1 = select_where_movie_is(movie1,movies_Db);
    castings2 = select_where_movie_is(movie2,movies_Db);
    commonActors = set(castings1).intersection(set(castings2));
    return list(commonActors);

def main():
    global actor_DB
    global ratings_DB
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')
    # PLEASE TAKE THE NEXT FEW PRINTING LINES OUT
    # ONCE YOU HAVE CONFIRMED THIS WORKS
    print "\tWelcome to Movie Database!\n"
    print "This database contains information of famous actors and actresses as well as \nmovie ratings.\n"
    print '''To use our database, please follow the instructions below:
    Press -1- for all movies the actor or actress has starred
    Press -2- for the cast of the movie
    Press -3- for all movies in certain rating range
    Press -4- for all actors or actresses the actor or actress has worked with 
    Press -5- for all movies starred by both actors or actresses
    Press -6- for the top rated actors or actresses by critics
    Press -7- for the top rated actors or actresses by audience
    Press -8- for the top rated movies
    Press -9- for the list of actors or actresses in both movies
    Press -#- for creating or updating new information about actors or actress
    Press -*- for deleting existing movie information
    Press -0- to exit\n'''

    choice = raw_input("\tPlease enter your option: ");
    while choice not in ['1','2','3','4','5','6','7','8','9','0']:
        choice = raw_input("\tError! Please enter your option again: ");
    

    
        
    
if __name__ == '__main__':
    main()
