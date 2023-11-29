import discord
from discord.ext import commands

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.add_command(self.hello)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} (ID: {self.user.id})')
        print('------')


client = MyBot(command_prefix='!')
client.run('MTE2ODU2NTkwMjUwNjIwOTM1Mg.GtN1Vl.ronvy9WGNx5hhcG5zVtotyjjIGqKj_ipPOzAqE')