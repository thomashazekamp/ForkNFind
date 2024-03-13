import unittest


from runner_sent_analysis import predict_sentiment

class testCasesSentimentAnalysis(unittest.TestCase):

    # Positive test cases

    def test_positive_sentiment(self): # Testing functionality of positive sentiment, using 'tfidf' and 'logistic_regression'
        self.assertEqual(predict_sentiment("I love this restaurant"), '1')

    def test_positive_sentimentv2(self):
        self.assertEqual(predict_sentiment("Great"), '1')
        
    def test_positive_sentimentv3(self):
        self.assertEqual(predict_sentiment("🤗 happy"), '1')

    def test_positive_sentimentv4(self):
        self.assertEqual(predict_sentiment("%%%333422%$$ Happy 22@@&&"), '1')


    # Negative test cases
    
    def test_negative_sentiment(self): # Testing functionality of negative sentiment, using 'tfidf' and 'logistic_regression'
        self.assertEqual(predict_sentiment("I hate this restaurant"), '0')

    def test_negative_sentimentv2(self):
        self.assertEqual(predict_sentiment("Terrible"), '0')

    def test_negative_sentimentv3(self):
        self.assertEqual(predict_sentiment("😔 sad"), '0')

    def test_negative_sentimentv4(self):
        self.assertEqual(predict_sentiment("%%%333422%$$ Sad 22@@&&"), '0')


    # Testing functionality of all vectorization types and model types
        
    # Count Vectorization
        
    def test_cv_logistic_regression(self):
        self.assertIn(predict_sentiment("I love this restaurant", 'cv', 'logistic_regression'), ['1', '0'])

    def test_cv_random_forest(self):
        self.assertIn(predict_sentiment("I hate this restaurant", 'cv', 'random_forest'), ['1', '0'])

    def test_cv_naive_bayes(self):
        self.assertIn(predict_sentiment("I love this restaurant", 'cv', 'naive_bayes'), ['1', '0'])

    def test_cv_support_vector_machine(self):
        self.assertIn(predict_sentiment("I hate this restaurant", 'cv', 'support_vector_machine'), ['1', '0'])

    def test_cv_gradient_boosting_machine(self):
        self.assertIn(predict_sentiment("I love this restaurant", 'cv', 'gradient_boosting_machine'), ['1', '0'])

    # TF-IDF Vectorization
    
    def test_tfidf_logistic_regression(self):
        self.assertIn(predict_sentiment("I hate this restaurant", 'tfidf', 'logistic_regression'), ['1', '0'])

    def test_tfidf_random_forest(self):
        self.assertIn(predict_sentiment("I love this restaurant", 'tfidf', 'random_forest'), ['1', '0'])

    def test_tfidf_naive_bayes(self):
        self.assertIn(predict_sentiment("I hate this restaurant", 'tfidf', 'naive_bayes'), ['1', '0'])

    def test_tfidf_support_vector_machine(self):
        self.assertIn(predict_sentiment("I love this restaurant", 'tfidf', 'support_vector_machine'), ['1', '0'])

    def test_tfidf_gradient_boosting_machine(self):
        self.assertIn(predict_sentiment("I hate this restaurant", 'tfidf', 'gradient_boosting_machine'), ['1', '0'])

    

if __name__ == '__main__':
    unittest.main()