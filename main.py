from utils.sonos_connector import custom_tts
import asyncio

def play(text):
    asyncio.run(custom_tts(text))