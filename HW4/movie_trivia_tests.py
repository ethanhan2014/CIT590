from movie_trivia import *
import unittest

class TestMovies(unittest.TestCase):

    movieDb = {}
    ratingDb = {}

    def setUp(self):
        self.movieDb = create_actors_DB('my_test_actors.txt')
        self.ratingDb = create_ratings_DB('my_ratings.csv')
    
    def testcreation(self):
         #check that movieDB got built
         self.assertTrue('Clint Eastwood' in self.movieDb.keys())
         #check that ratingDB has been built
         self.assertTrue('Gran Torino' in self.ratingDb.keys())
         self.assertEqual(self.ratingDb['Gran Torino'], ['87', '93'])
         #double check
         self.assertFalse('Jackie Chan' in self.movieDb.keys())
         #check that ratingDB has been built
         self.assertFalse('Rush Hour' in self.ratingDb.keys())
         self.assertNotEqual(self.ratingDb['Gran Torino'], ['78', '93'])

    def testinsertion_delete(self):
        #create an actor's info
        insert_actor_info('Jackie Chan',['Rush Hour'],self.movieDb)
        insert_rating('Rush Hour',(70,80),self.ratingDb)
        #check that the info has been built
        self.assertTrue('Jackie Chan' in self.movieDb.keys())
        self.assertTrue('Rush Hour' in self.ratingDb.keys())
        self.assertEqual(self.ratingDb['Rush Hour'], ['70', '80'])
        #delete a movie's info
        delete_movie('Rush Hour',self.movieDb,self.ratingDb)
        #check that the movie has been deleted
        self.assertFalse('Rush Hour' in self.ratingDb.keys(),'A movie deleted')
        

    def testselect_where_movie_is(self):
        #write test code here using self.ratingDb and self.movieDb
        actors = set(select_where_movie_is('Mr & Mrs Smith', self.movieDb))
        #make some assertion about these actors
        self.assertEqual(set(['Brad Pitt','Angelina Jolie']),actors)

    def testselect_where_actor_is(self):
        #check actor's info
        self.assertEqual(['Gran Torino'],
                         select_where_actor_is('Clint Eastwood',self.movieDb));
        #double check
        self.assertNotEqual(['Rush Hour'],
                            select_where_actor_is('Clint Eastwood',self.movieDb));
        
    def testselect_where_rating_is(self):
        #check whether the function works
        movie1 = select_where_rating_is(100,'=', True, self.ratingDb)
        self.assertEqual(['The Philadelphia Story'],movie1)
        movie2 = select_where_rating_is(99,'=', False, self.ratingDb)
        self.assertNotEqual(['The Philadelphia Story'],movie2)
        movie3 = select_where_rating_is(60,'<', True, self.ratingDb)
        self.assertEqual(['Mr & Mrs Smith'],movie3)
        movie4 = select_where_rating_is(60,'=', False, self.ratingDb)
        self.assertEqual([],movie4)

    def testget_co_actors(self):
        co_actors = set(get_co_actors('Tom Hanks',self.movieDb))
        self.assertEqual(set(['Leonardo Di Caprio','Meg Ryan']),co_actors)
        co_actors2 = set(get_co_actors('Clint Eastwood',self.movieDb))
        self.assertEqual(set([]),co_actors2)
        
    def testget_common_movie(self):
        movies = set(get_common_movie('Leonardo Di Caprio','Tom Hanks'
                                      ,self.movieDb))
        self.assertEqual(set(['Catch Me If You Can']),movies)

    def testcritics_darling(self):
        self.assertTrue('Tom Hanks' in
                        critics_darling(self.movieDb,self.ratingDb))

    def testaudience_darling(self):
        self.assertTrue('Tom Hanks' in
                        critics_darling(self.movieDb,self.ratingDb))

    def testgood_movies(self):
        movies = set(good_movies(self.ratingDb))
        self.assertEqual(set(['Gran Torino','The Philadelphia Story',
                              'Catch Me If You Can']),movies)
        
    def testget_common_actors(self):
        actors = set(get_common_actors('Philadelphia',
                                   'Catch Me If You Can',self.movieDb))
        self.assertEqual(set(['Tom Hanks']),actors)
        

    #write unit tests for every function.
                
unittest.main()
