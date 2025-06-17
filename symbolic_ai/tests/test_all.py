from ..core import symbolic_test_suite
from ..vision import test_vision
from ..audio import test_audio
from ..web import test_web
from ..cognition import test_cognition
from ..creativity import test_creativity
from ..tools import test_tools


def test_self_check():
    assert symbolic_test_suite.self_check()


def test_vision_suite():
    test_vision.test_train()
    test_vision.test_identify()
    test_vision.test_decode()
    test_vision.test_live_reader()


def test_audio_suite():
    test_audio.test_link()
    test_audio.test_map()
    test_audio.test_extract()


def test_web_suite():
    test_web.test_crawl()
    test_web.test_learn()
    test_web.test_query()


def test_cognition_suite():
    test_cognition.test_meaning()
    test_cognition.test_discover()
    test_cognition.test_emotion()


def test_creativity_suite():
    test_creativity.test_poet()
    test_creativity.test_art()
    test_creativity.test_language()


def test_tools_suite():
    test_tools.test_camera()
    test_tools.test_browser()
    test_tools.test_transcriber()
    test_tools.test_font_downloader()
