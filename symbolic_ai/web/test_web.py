import unittest

from .web_letter_crawler import WebLetterCrawler
from .youtube_letter_learner import YouTubeLetterLearner
from .deepseek_ai_connector import DeepSeekAIConnector


class TestWeb(unittest.TestCase):
    def test_crawl(self):
        crawler = WebLetterCrawler()
        self.assertIn("hello", crawler.crawl("http://example.com/hello"))

    def test_learn(self):
        learner = YouTubeLetterLearner()
        self.assertTrue(learner.learn("http://yt"))

    def test_query(self):
        connector = DeepSeekAIConnector()
        self.assertEqual(connector.query("hi"), "HI")


if __name__ == "__main__":
    unittest.main()
