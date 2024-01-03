import json


def checkIfFieldInNextItem(c, f: str):
    if isinstance(c, dict):
        if f in c.keys():
            return True
    return False


def get_data(file_path, data_path):
    with open(file_path, "r") as file:
        content = json.loads("".join([line for line in file.readlines()]))
        if str(content) == "":
            return ""
        for module in str(data_path).rstrip().lstrip().split("."):
            if checkIfFieldInNextItem(content, module):
                content = content.get(module)
            else:
                return None
        return content


def save_data(file_path, data_path, data):
    with open(file_path, "r+") as file:
        content:dict = json.loads("".join([line for line in file.readlines()]))
        args = str(data_path).rstrip().lstrip().split(".")
        temp = content.copy()
        for mod in args[:-1]:
            temp = temp.get(mod)
            print(temp)
        temp.update({args[-1]: data})

        file.write(temp)

save_data("test.json", "hello.world.test", "holaa")