import os.path

from cryptography.fernet import Fernet as fer

def encryptConfigFile(path):
    if os.path.exists(path):
        content = None
        with open(path, "r") as file:
            content = "".join(file.readlines())
    else:
        pass