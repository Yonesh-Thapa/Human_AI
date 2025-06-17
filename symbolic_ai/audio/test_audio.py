import unittest

from .speech_letter_linker import SpeechLetterLinker
from .letter_to_sound_mapper import LetterToSoundMapper
from .video_speech_extractor import VideoSpeechExtractor


class TestAudio(unittest.TestCase):
    def test_link(self):
        linker = SpeechLetterLinker()
        self.assertEqual(linker.link("a"), ["A"])

    def test_map(self):
        mapper = LetterToSoundMapper()
        self.assertEqual(mapper.map("b"), "bee")

    def test_extract(self):
        extractor = VideoSpeechExtractor()
        data = extractor.extract(b"hello")
        self.assertIsInstance(data, bytes)


if __name__ == "__main__":
    unittest.main()
