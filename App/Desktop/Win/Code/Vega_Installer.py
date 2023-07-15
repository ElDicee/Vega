import os
import sys

import App.Desktop.Win.Code.installer as installer
from PySide6.QtWidgets import QApplication

ORIGIN_VEGA_FOLDER_NAME = ".vega"
VEGA_ORIGIN_FILE_NAME = "VegaOrigins"
VEGA_ORIGIN_FILE_NAME_EXT = VEGA_ORIGIN_FILE_NAME + ".vg"


# MIRAR SI EXISTEIX LA CARPETA VEGA A LA RUTA ROAMING, SI NO GENERAR-LA.
# MIRAR SI A DINS DE LA CARPETA EXISTEIX L'ARXIU VegaOrigins.vg, EN CAS CONTRARI GENERAR-LO.
def checkVegaRoamingFolder(app):
    global path
    path = os.getenv("APPDATA")
    b = ORIGIN_VEGA_FOLDER_NAME in os.listdir(path)
    path += f"\{ORIGIN_VEGA_FOLDER_NAME}"
    if b:
        with os.scandir(path) as scan:
            b = False
            for entry in scan:
                if entry.is_file():
                    if entry.name == VEGA_ORIGIN_FILE_NAME_EXT:
                        b = True
                        break
            if not b:
                f = open(path + f"\{VEGA_ORIGIN_FILE_NAME_EXT}", "w")
                f.close()
    else:
        os.mkdir(path)
        with open(path + f"\{VEGA_ORIGIN_FILE_NAME_EXT}", "w") as file:
            file.close()
    installFiles(app)
    return b


def runInstaller(app):
    ui = installer.Installer()
    ui.show()
    app.exec()


def installFiles(app):
    with open(f"{path}\{VEGA_ORIGIN_FILE_NAME_EXT}", "r") as origin:
        if origin.readlines().__len__() <= 0:
            if "VegaPath:" not in "".join(origin.readlines()):
                print(origin.readlines().__len__())
                origin.close()
                runInstaller(app)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    installedFiles = checkVegaRoamingFolder(app)
