import json
import os

class Lang():
    def __init__(self, language:str):
        self.language:str = language
        self.filepath = f"langs/{self.language}.json"
        self.content = None
        with open(self.filepath, "r") as file:
            self.content = json.loads("".join(file.readlines()))
"""with open("langs/es_SP.json", "r") as file:
    print(file.readlines())"""
Lang("es_SP")