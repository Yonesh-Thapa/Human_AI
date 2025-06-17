import unittest

from .camera_handler import CameraHandler
from .browser_reader import BrowserReader
from .speech_transcriber import SpeechTranscriber
from .font_downloader import FontDownloader


class TestTools(unittest.TestCase):
    def test_camera(self):
        cam = CameraHandler()
        self.assertIsNotNone(cam.capture())

    def test_browser(self):
        br = BrowserReader()
        self.assertEqual(br.read("<p>hi</p>"), "hi")

    def test_transcriber(self):
        tr = SpeechTranscriber()
        self.assertEqual(tr.transcribe(b"hi"), "hi")

    def test_font_downloader(self):
        fd = FontDownloader()
        self.assertTrue(fd.download("arial"))


if __name__ == "__main__":
    unittest.main()
