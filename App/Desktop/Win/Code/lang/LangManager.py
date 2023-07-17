import json
import os
import enum


ENGLISH = "US_en"
SPANISH = "SP_es"
CATALAN = "SP_cat"
class Lang():
    def __init__(self, language: str = "en"):
        self.content = None
        self.language: str = language
        self.load(self.language)

    def get(self, s:str):
        a = self.content
        for arg in s.split("."):
            a = a[arg]
        return a

    def load(self, code:str):
        self.filepath = f"langs/{self.language}.json"
        with open(self.filepath, "r") as file:
            self.content = json.loads("".join(file.readlines()))


if __name__ == "__main__":
    l = Lang(language=ENGLISH)