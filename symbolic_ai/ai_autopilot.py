class AutonomousAI:
    def __init__(self, source: str):
        from symbolic_ai.vision.live_reader import VisionReader
        from symbolic_ai.audio.live_listener import VoiceListener
        from symbolic_ai.web.web_downloader import WebDownloader
        from symbolic_ai.logic.logic_chain import LogicChain
        from symbolic_ai.core.memory_manager import MemoryManager
        from symbolic_ai.tools.live_debugger import Debugger
        from symbolic_ai.deepseek_interface import DeepSeekInterface

        self.source = source
        self.memory = MemoryManager()
        self.debugger = Debugger()
        self.logic = LogicChain(self.memory)
        self.deepseek = DeepSeekInterface()
        self.vision = VisionReader()
        self.voice = VoiceListener()
        self.web = WebDownloader()

    def run(self) -> None:
        """Main autonomous loop that improves itself over time."""
        import time

        url: str | None = None
        while True:
            self.debugger.update(f"Learning from: {self.source}")
            if self.source == "camera":
                symbols = self.vision.scan()
            elif self.source == "voice":
                symbols = self.voice.listen()
            elif self.source == "web":
                if url is None:
                    url = input("Enter URL: ")
                symbols = self.web.fetch(url)
            else:
                print("❌ Invalid source")
                return

            for sym in symbols:
                pattern = {"symbol": sym, "vector": [ord(sym)]}
                self.memory.store(sym, pattern)
            if symbols:
                self.debugger.log(f"🧠 Learned: {symbols}")

            suggestion = self.deepseek.clarify("What symbolic logic should I learn next?")
            if suggestion:
                pattern = {"symbol": suggestion, "vector": [ord(suggestion[0]) if suggestion else 0]}
                self.memory.store(suggestion, pattern)
                self.debugger.log(f"📡 DeepSeek: {suggestion}")

            replay = [p["symbol"] for p in self.memory.replay()]
            self.debugger.log(f"🔁 Thinking: {replay}")
            self.logic.process(replay)
            chain = self.logic.explain(replay[0]) if replay else []
            if chain:
                self.debugger.log(f"➿ Reasoning: {chain}")

            self._self_improve()
            time.sleep(2)

    def _self_improve(self) -> None:
        """Trivial self improvement by trimming old patterns."""
        if len(self.memory.replay()) > 20:
            for sym, pats in self.memory.memory.items():
                self.memory.memory[sym] = pats[-10:]
            self.debugger.log("🛠 Memory trimmed for self-improvement")

