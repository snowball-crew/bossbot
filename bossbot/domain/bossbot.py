import os

from discord import Intents
from discord.ext.commands import Bot
from dotenv import load_dotenv


class BossBot(Bot):
    def __init__(self):
        self.token = self._get_token()
        super().__init__(
            command_prefix="!",
            intents=Intents.all(),
        )

    def run(self, *args, **kwargs):
        super().run(self.token, *args, **kwargs)

    @staticmethod
    def _get_token():
        load_dotenv()
        return os.getenv("DISCORD_BOT_TOKEN")
