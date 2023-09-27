import discord
import App.Desktop.Win.Extern.VegaExternEventAdapter as adapter


class MiniSenku(discord.client):
    async def on_ready(self):
        print("Stablishing server...")
        self.vega_server = adapter.VegaClient_Server("MiniSenku 2.0", "127.0.0.1", 8797)
        print("Connected!")

    async def on_message(self):
        pass

intents = discord.Intents.default()
intents.message_content = True

client = MiniSenku(intents=intents)
client.run("")