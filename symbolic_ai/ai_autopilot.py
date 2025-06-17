class AutonomousAI:
    def __init__(self, source: str):
        from symbolic_ai.vision.live_reader import VisionReader
        from symbolic_ai.audio.live_listener import VoiceListener
        from symbolic_ai.web.web_searcher import WebSearcher
        from symbolic_ai.logic.logic_chain import LogicChain
        from symbolic_ai.core.memory_manager import MemoryManager
        from symbolic_ai.tools.live_debugger import Debugger
        from symbolic_ai.web.deepseek_connector import DeepSeekConnector

        self.source = source
        self.memory = MemoryManager()
        self.debugger = Debugger()
        self.logic = LogicChain(self.memory)
        self.deepseek = DeepSeekConnector()
        self.vision = VisionReader()
        self.voice = VoiceListener()
        self.web = WebSearcher()

    def run(self) -> None:
        import time

        while True:
            self.debugger.update(f"Learning from: {self.source}")
            if self.source == "camera":
                symbols = self.vision.scan()
            elif self.source == "voice":
                symbols = self.voice.listen()
            elif self.source == "web":
                symbols = self.web.extract_symbols()
            else:
                print("❌ Invalid source")
                return

            for sym in symbols:
                pattern = {"symbol": sym, "vector": [ord(sym)]}
                self.memory.store(sym, pattern)
            self.debugger.log(f"🧠 Learned: {symbols}")

            suggestion = self.deepseek.ask("What symbolic logic should I learn next?")
            if suggestion:
                pattern = {"symbol": suggestion, "vector": [ord(suggestion[0]) if suggestion else 0]}
                self.memory.store(suggestion, pattern)
            self.debugger.log(f"📡 DeepSeek: {suggestion}")

            replay = [p["symbol"] for p in self.memory.replay()]
            self.debugger.log(f"🔁 Thinking: {replay}")
            self.logic.process(replay)
            time.sleep(5)

