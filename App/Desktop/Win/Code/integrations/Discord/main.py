from typing import Any

import discord
from discord.ext import commands

import App.Desktop.Win.Code.integrations.VegaAPI as api
from App.Desktop.Win.Code.integrations.Discord import vega_ui

ITG_NAME = "DiscordBot"
DISCORD_EVENT = api.Event("DC_Data", ITG_NAME, outputs={"Text": str, "Guild": str, "Channel": str, "Author": str})


class VegaDCBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="%", intents=intents)
        self.conn = None

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

    async def on_message(self, msg):
        self.send_data(DISCORD_EVENT, {"Channel": msg.channel.name, "Guild": msg.guild.name, "Author": msg.author.name,
                                       "Text": msg.content})


def vega_main():
    form = vega_ui.Ui_Form()
    vega = api.Vega_Portal()
    vega.set_name(ITG_NAME)
    vega.add_display_screen(form)
    vega.add_event(DISCORD_EVENT)
    m = api.Method(form.add_label, api.EXECUTION, formal_name="Add Label To Registry")
    vega.add_display_method(m)
    print(m.func)
    return vega


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


if __name__ == "__main__":
    bot = VegaDCBot()
    bot.run("MTE2ODU2NTkwMjUwNjIwOTM1Mg.G5daDz.hoic_r0eTrNnLn1VhOSlMEPDkS2Ex7yHuZfbHY")
