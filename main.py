from symbolic_ai.core.learning_loop import LearningLoop
from symbolic_ai.core.memory_manager import MemoryManager
from symbolic_ai.tools.live_debugger import LiveDebugger
from symbolic_ai.web.web_letter_crawler import WebLetterCrawler


def main():
    memory = MemoryManager()
    loop = LearningLoop(memory)
    debug = LiveDebugger(memory)

    mode = input("Input method (camera/voice/web): ").strip().lower()
    if mode == "camera":
        loop.learn_from_camera()
    elif mode == "voice":
        data = input("Say something: ").encode("utf-8")
        loop.learn_from_voice(data)
    elif mode == "web":
        url = input("Enter URL: ")
        crawler = WebLetterCrawler()
        text = crawler.crawl(url)
        loop.learn_from_text(text)
    else:
        print("Unknown mode")

    debug.display()


if __name__ == "__main__":
    main()
