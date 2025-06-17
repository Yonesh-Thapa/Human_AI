from .camera_handler import CameraHandler
from .browser_reader import BrowserReader
from .speech_transcriber import SpeechTranscriber
from .font_downloader import FontDownloader


def test_camera():
    cam = CameraHandler()
    assert cam.capture() is None

def test_browser():
    br = BrowserReader()
    assert br.read('') == ''

def test_transcriber():
    tr = SpeechTranscriber()
    assert tr.transcribe(None) == ''

def test_font_downloader():
    fd = FontDownloader()
    assert fd.download('arial')
