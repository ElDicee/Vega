import os
import importlib.util
import sys


def loada(path):
    for folder in os.listdir(path):
        spec = importlib.util.spec_from_file_location(folder, f"{path}/{folder}/main.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.main()


def unloadModule(spec):
    del sys.modules[spec.name]


def load():
    spec = importlib.util.spec_from_file_location("Basics", f"integrations/Basics/main.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    v = mod.vega_main()