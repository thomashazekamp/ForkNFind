import unittest


from runner_sent_analysis import predict_sentiment

class testCasesSentimentAnalysis(unittest.TestCase):

    # Positive test cases

    def test_positive_sentiment(self): # Testing functionality of positive sentiment
        self.assertEqual(predict_sentiment("I love this restaurant"), '1')

    def test_positive_sentimentv2(self):
        self.assertEqual(predict_sentiment("Great"), '1')
        
    def test_positive_sentimentv3(self):
        self.assertEqual(predict_sentiment("🤗 happy"), '1')

    def test_positive_sentimentv4(self):
        self.assertEqual(predict_sentiment("%%%333422%$$ Happy 22@@&&"), '1')

    # Negative test cases
    
    def test_negative_sentiment(self): # Testing functionality of negative sentiment
        self.assertEqual(predict_sentiment("I hate this restaurant"), '0')

    def test_negative_sentimentv2(self):
        self.assertEqual(predict_sentiment("Terrible"), '0')

    def test_negative_sentimentv3(self):
        self.assertEqual(predict_sentiment("😔 sad"), '0')

    def test_negative_sentimentv4(self):
        self.assertEqual(predict_sentiment("%%%333422%$$ Sad 22@@&&"), '0')

if __name__ == '__main__':
    unittest.main()