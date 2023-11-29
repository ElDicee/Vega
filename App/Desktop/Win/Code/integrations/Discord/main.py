import App.Desktop.Win.Code.integrations.VegaAPI as api


ITG_NAME = "DiscordBot"
DISCORD_EVENT = api.Event("Message Sent From Discord", ITG_NAME, outputs={"Message": str})


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name(ITG_NAME)
    vega.add_event(DISCORD_EVENT)


if __name__ == "__main__":
    pass
