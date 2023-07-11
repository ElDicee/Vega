# POSSIBLE FEATURES
#  - Adding custom themes by user

import os, json, PySide6

CONFIG_PATH = "../config/config.json"


class Vega:
    def __init__(self):
        pass

    def renderUI(self):
        pass

    @classmethod
    def checkDefaults(self):
        if not "config" in os.listdir("../"):
            os.mkdir("../config")

        with os.scandir("../config") as scan:
            f = ["config.json", "theme_dark.json", "theme_light.json"]
            # DETECTING EXISTING CONFIG FILES
            for entry in scan:
                if entry.is_file():
                    if entry.name == "config.json":
                        f.remove("config.json")
                    elif entry.name == "theme_dark.json":
                        f.remove("theme_dark.json")
                    elif entry.name == "theme_light.json":
                        f.remove("theme_light.json")
            # GENERATING CONFIG FILES THAT DOESN'T EXIST
            if "config.json" in f:
                with open(CONFIG_PATH, "w") as file:
                    file.write("""{"setup": true,
                    "lang": "cat_SP",
                    "theme": "Dark"}""")
            if "theme_dark.json" in f:
                with open("../config/theme_dark.json") as scheme:
                    # CONFIGURATION OF COLOR SCHEME
                    pass
        # LOADING CONFIGURATION FILES
        with open(CONFIG_PATH, "r") as file:
            config = json.loads("".join([line for line in file.readlines()]))
            if config["setup"]:
                # config during first installation
                pass
            else:
                lang = config["lang"]
                theme = config["theme"]

    def saveConfiguration(self):
        pass

    def loadConfiguration(self):
        pass


if __name__ == "__main__":
    Vega().checkDefaults()
