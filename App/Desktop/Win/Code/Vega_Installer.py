import os

VEGA_ORIGIN_FILE_NAME = "VegaOrigins"
VEGA_ORIGIN_FILE_NAME_EXT = VEGA_ORIGIN_FILE_NAME+".vg"


#MIRAR SI EXISTEIX LA CARPETA VEGA A LA RUTA ROAMING, SI NO GENERAR-LA.
#MIRAR SI A DINS DE LA CARPETA EXISTEIX L'ARXIU VegaOrigins.vg, EN CAS CONTRARI GENERAR-LO.
def checkVegaRoamingFolder():
    global path
    path = os.getenv("APPDATA")
    b = "Vega" in os.listdir(path)
    path += "\Vega"
    if b:
        with os.scandir(path) as scan:
            b = "VegaOrigins.vg" in scan
            if not b:
                f = open(path+f"\{VEGA_ORIGIN_FILE_NAME_EXT}", "w")
                f.close()
    else:
        os.mkdir(path)
        f = open(path + f"\{VEGA_ORIGIN_FILE_NAME_EXT}", "w")
        f.close()
    return b

def installFiles():
    with open(path, "r+") as origin:
        if not "VegaPath:" in origin.readlines()[0]:
            pass

if __name__ == "__main__":
    installedFiles = checkVegaRoamingFolder()
