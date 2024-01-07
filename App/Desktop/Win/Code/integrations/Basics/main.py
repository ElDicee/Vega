import App.Desktop.Win.Code.integrations.VegaAPI as api


def not_sent(boolean: bool):
    return not boolean


def equal(element1, element2):
    return element1 == element2


def not_equal(element1, element2):
    return not element1 == element2


def is_in(element, group):
    return element in group


# LISTS---------------------------------LISTS---------------------------------LISTS---------------------------------LISTS---------------------------------


def get_item_by_index(list, index: int):
    return list[index]


# STRING-------------------------------------STRING-------------------------------------STRING-------------------------------------STRING-------------------------------------

def to_str(element):
    return str(element)


def _split(string: str, char: str):
    return string.split(char)


# MATH--------------------------------------MATH--------------------------------------MATH--------------------------------------MATH--------------------------------------

def to_int(element):
    return int(element)


# LIST AND DICT OPERATIONS


def create_empty_list():
    return []


def get_list_item(list, index: int):
    return list[index]


def add_list_item(list, item):
    list.append(item)


def lenght(element):
    return len(element)


def create_empty_dictionary():
    return {}


def get_dict_value(dict, key):
    return dict.get(key)


def get_dict_keys(dict):
    return list(dict.keys())


def get_dict_values(dict):
    return list(dict.values())


def update_dict(dict, key, value):
    dict.update({key, value})
    return dict


def if_pol(f, condition: bool):
    return f("TRUE") if condition else f("FALSE")


def elseif_pol(f, condition1: bool, condition2: bool):
    if condition1:
        f("OPT1")
    elif condition2:
        f("OPT2")
    else:
        f("ELSE")


def for_each_pol(f, list):
    for e in list:
        f("ITERATION", {"Element": e})
    f("FINISHED")


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("Basics")
    vega.add_method(api.Method(not_sent, api.OPERATOR, outputs={"result": bool}, formal_name="NOT"))
    vega.add_method(
        api.Method(create_empty_list, api.EXECUTION, outputs={"List": None}, formal_name="Create Empty List"))
    vega.add_method(api.Method(get_list_item, api.OPERATOR, outputs={"Item": None}, formal_name="Get List Item"))
    vega.add_method(api.Method(add_list_item, api.EXECUTION, formal_name="Add List Item"))
    vega.add_method(api.Method(lenght, api.OPERATOR, outputs={"Lenght": int}, formal_name="Lenght"))
    vega.add_method(api.Method(to_str, api.OPERATOR, outputs={"String": str}, formal_name="To String"))
    vega.add_method(api.Method(to_int, api.OPERATOR, outputs={"Integer": int}, formal_name="To Integer"))
    vega.add_method(api.Method(is_in, api.OPERATOR, outputs={"Is Inside": bool}, formal_name="Is Inside"))
    vega.add_method(api.Method(_split, api.OPERATOR, outputs={"Elements": None}, formal_name="Split"))
    vega.add_method(api.Method(equal, api.OPERATOR, outputs={"Result": bool}, formal_name="Equals"))
    vega.add_method(api.Method(not_equal, api.OPERATOR, outputs={"Result": bool}, formal_name="Not Equals"))
    vega.add_method(api.Method(create_empty_dictionary, api.EXECUTION, outputs={"Dict": None},
                               formal_name="Create Empty Dictionary"))
    vega.add_method(api.Method(get_dict_value, api.OPERATOR, outputs={"Value": None}, formal_name="Get Dict Value"))
    vega.add_method(api.Method(get_dict_keys, api.OPERATOR, outputs={"Keys List": None}, formal_name="Get Dict Keys"))
    vega.add_method(api.Method(not_equal, api.OPERATOR, outputs={"Values List": None}, formal_name="Get Dict Values"))
    vega.add_method(api.Method(update_dict, api.EXECUTION, outputs={"Dict": None}, formal_name="Update Dict Value"))

    if_sp = api.SpecialMethod(None, api.EXECUTION, formal_name="If Else")
    if_sp.add_execution_output("TRUE")
    if_sp.add_execution_output("FALSE")
    if_sp.set_execution_policy(if_pol)
    vega.add_method(if_sp)

    elif_sp = api.SpecialMethod(None, api.EXECUTION, formal_name="Elif Else")
    elif_sp.add_execution_output("OP1")
    elif_sp.add_execution_output("OPT2")
    elif_sp.add_execution_output("ELSE")
    elif_sp.set_execution_policy(elseif_pol)
    vega.add_method(elif_sp)

    foreach_sp = api.SpecialMethod(None, api.EXECUTION, outputs={"Element": None}, formal_name="For Each Loop")
    foreach_sp.add_execution_output("ITERATION")
    foreach_sp.add_execution_output("FINISHED")
    foreach_sp.set_execution_policy(for_each_pol)
    vega.add_method(foreach_sp)

    return vega
