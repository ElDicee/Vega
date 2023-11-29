from typing import Any

import discord
from discord.ext import commands

import App.Desktop.Win.Code.integrations.VegaAPI as api

ITG_NAME = "DiscordBot"
DISCORD_EVENT = api.Event("DC_Data", ITG_NAME, outputs={"Data": str, "Channel": str})

intents = discord.Intents.default()
intents.message_content = True


class VegaDCBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="%", intents=intents)
        self.conn = None
        self.add_command(self.test)

    def send_data(self, event, data):
        if self.conn:
            if self.conn.is_closing:
                try:
                    self.conn = api.VegaConnection(False)
                    self.send_data(event, data)
                except:
                    print("Could not connect to Vega Portal.")
            else:
                self.conn.emit(event, data)
        else:
            try:
                self.conn = api.VegaConnection(False)
                self.send_data(event, data)
            except:
                print("Could not connect to Vega Portal.")

    async def on_ready(self):
        try:
            self.conn = api.VegaConnection(False)
        except:
            self.conn = None
            print("Could not connect to Vega!!")
        print("Bot is ready!")

    @commands.command(name="test")
    async def test(self, ctx, *args):
        text = " ".join(args)
        self.send_data(DISCORD_EVENT, text)
        await ctx.send(text)


bot = VegaDCBot()


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name(ITG_NAME)
    vega.add_event(DISCORD_EVENT)


# @bot.event
# async def on_ready():
#     try:
#         pass
#     except:
#         connection = None
#         print("Could not connect to Vega!!")
#     print("Bot is ready!")


# @bot.command(name="test")
# async def test_com(ctx, *args):
#     text = " ".join(args)
#     await ctx.send(text)


bot.run("MTE2ODU2NTkwMjUwNjIwOTM1Mg.G1SZFF.V-XShmzAcS2ikHWssuqvU8WWJ9SGfZlFXwhFu8")
