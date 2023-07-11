import os
import importlib.util
import sys

def load2(path):
    for folder in os.listdir(path):
        spec = importlib.util.spec_from_file_location(folder, f"{path}/{folder}/main.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.main()
load2("integrations")

def unloadModule(spec):
    del sys.modules[spec.name]