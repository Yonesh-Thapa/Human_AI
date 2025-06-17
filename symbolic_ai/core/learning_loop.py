from symbolic_ai.core.brain_controller import BrainController
from symbolic_ai.core.memory_manager import MemoryManager
from symbolic_ai.audio.speech_to_letter import SpeechToLetter
from symbolic_ai.vision.camera_reader import CameraReader
from symbolic_ai.logic.pattern_discoverer import PatternDiscoverer
from symbolic_ai.logic.symbol_recognizer import SymbolRecognizer
from symbolic_ai.logic.logic_chain import LogicChain
from symbolic_ai.tools.live_debugger import Debugger
from symbolic_ai.deepseek_interface import DeepSeekInterface


class LearningLoop:
    """Coordinate symbol learning from various modalities."""

    def __init__(self, memory: MemoryManager):
        self.memory = memory
        self.brain = BrainController(memory)
        self.discoverer = PatternDiscoverer()
        self.recognizer = SymbolRecognizer(memory)
        self.chain = LogicChain()
        self.camera = CameraReader()
        self.speech = SpeechToLetter()
        self.debugger = Debugger()
        self.deepseek = DeepSeekInterface()
        self.last_symbol: str | None = None

    def learn_symbol(self, symbol: str) -> dict:
        pattern = self.brain.run(symbol)
        if self.last_symbol is not None:
            self.chain.add_link(self.last_symbol, symbol)
        self.last_symbol = symbol
        # cluster all patterns for abstraction
        patterns = [p for pats in self.memory.memory.values() for p in pats]
        clusters = self.discoverer.cluster(patterns)
        return {"pattern": pattern, "clusters": clusters}

    def learn_from_camera(self) -> dict:
        letter = self.camera.read_letter()
        return self.learn_symbol(letter)

    def learn_from_voice(self, audio: bytes) -> dict:
        letter = self.speech.convert(audio)
        if letter:
            return self.learn_symbol(letter)
        return {}

    def learn_from_text(self, text: str) -> dict:
        result = {}
        for ch in text:
            if ch.isalpha() or ch.isdigit():
                result = self.learn_symbol(ch)
        return result

    def run_autonomous(self, source: str) -> None:
        """Continuously learn from the chosen source and log progress."""
        import time

        while True:
            if source == "camera":
                symbols = [self.camera.read_letter()]
            elif source == "voice":
                symbols = self.speech.listen()
            elif source == "web":
                question = "Give me more symbols"
                answer = self.deepseek.clarify(question)
                symbols = [ch for ch in answer if ch.isalpha()]
            else:
                self.debugger.log("Invalid source")
                return

            for sym in symbols:
                info = self.learn_symbol(sym)
                self.debugger.log(f"Learned {sym}: {info['pattern']}")

            # ask deepseek for follow-up
            if symbols:
                ask = f"What should I know about {symbols[-1]}?"
                response = self.deepseek.clarify(ask)
                if response:
                    self.debugger.log(f"DeepSeek says: {response}")

            sequence = [p["symbol"] for p in self.memory.replay()]
            self.chain.process(sequence)
            self.debugger.update(f"Logic links: {len(self.chain.links)}")
            time.sleep(1)
