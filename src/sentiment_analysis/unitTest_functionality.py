import unittest


from runner_sent_analysis import predict_sentiment

class testCasesSentimentAnalysis(unittest.TestCase):

    def test_positive_sentiment(self): # Testing functionality of positive sentiment
        self.assertEqual(predict_sentiment("I love this restaurant"), '1')
    
    def test_negative_sentiment(self): # Testing functionality of negative sentiment
        self.assertEqual(predict_sentiment("I hate this restaurant"), '0')

if __name__ == '__main__':
    unittest.main()