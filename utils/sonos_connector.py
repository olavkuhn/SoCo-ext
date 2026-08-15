import soco
import tomllib
from sonos_websocket import SonosWebsocket
from utils.tts import TTSGenerator

with open("config.toml", "rb") as f:
    config = tomllib.load(f)


async def custom_tts(input_text: str, volume: int = 2):
    speaker = SonosWebsocket(config['target_ip'])

    tts = TTSGenerator()
    tts.generate_file(f"{input_text}", "t1.mp3")

    try:
        await speaker.play_clip(uri="")
    except Exception as e:
        print(f"Something went wrong playing a custom TTS: {e}")