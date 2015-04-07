from Cards import * 
import unittest

class Test_Card(unittest.TestCase):

    def setUp(self):
        self.card1 = Card('a','c')
        self.card2 = Card(5,'d')
        self.assertRaises(RuntimeError, Card, 1,'d')
        self.assertRaises(RuntimeError, Card, 5,2)
        self.assertRaises(RuntimeError, Card,'','')
        self.assertRaises(RuntimeError, Card,5,'')
        self.assertEqual('AC',str(self.card1))
        self.assertEqual('5D',str(self.card2))
        
    def testget_rank(self):
        self.assertEqual('A',self.card1.get_rank());
        self.assertEqual(5,self.card2.get_rank());

    def testget_suit(self):
        self.assertEqual('C',self.card1.get_suit());
        self.assertEqual('D',self.card2.get_suit());

class Test_Deck(unittest.TestCase):
    
    def setUp(self):
        self.tdeck = Deck()

    def test_shuffle(self):
        self.tdeck.shuffle()
        self.assertEqual(52,len(self.tdeck.get_deck()))
        self.assertNotEqual('2S',str(self.tdeck.get_deck()[0]))
        self.assertNotEqual('AH',str(self.tdeck.get_deck()[-1]))

    def test_deal(self):
        self.tdeck.deal()
        self.assertEqual(51,len(self.tdeck.get_deck()))
        self.tdeck.deal()
        self.assertEqual(50,len(self.tdeck.get_deck()))

    def testget_deck(self):
        self.assertTrue(type(self.tdeck.get_deck()) is list)
        self.assertEqual(52,len(self.tdeck.get_deck()))
        

unittest.main()
