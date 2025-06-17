from .speech_letter_linker import SpeechLetterLinker
from .letter_to_sound_mapper import LetterToSoundMapper
from .video_speech_extractor import VideoSpeechExtractor


def test_link():
    linker = SpeechLetterLinker()
    assert linker.link(None) == []

def test_map():
    mapper = LetterToSoundMapper()
    assert mapper.map('a') == 'sound'

def test_extract():
    extractor = VideoSpeechExtractor()
    assert extractor.extract(None) == b""
