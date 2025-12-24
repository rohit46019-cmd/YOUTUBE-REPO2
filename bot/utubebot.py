from pyrogram import Client
from config import Config

class UtubeBot(Client):
    def __init__(self):
        super().__init__(
            session_name=Config.SESSION_NAME,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=6,
        )
