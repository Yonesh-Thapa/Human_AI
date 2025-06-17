from .web_letter_crawler import WebLetterCrawler
from .youtube_letter_learner import YouTubeLetterLearner
from .deepseek_ai_connector import DeepSeekAIConnector


def test_crawl():
    crawler = WebLetterCrawler()
    assert crawler.crawl('') == ''

def test_learn():
    learner = YouTubeLetterLearner()
    assert learner.learn('')

def test_query():
    connector = DeepSeekAIConnector()
    assert connector.query('hi') == 'response'
