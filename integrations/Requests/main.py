import integrations.VegaAPI as api
import requests


def get_m(url: str = "www.google.com"):
    return requests.get(url)


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("Requests")
    vega.add_method(api.Method(get_m, api.OPERATOR, outputs={"Response": None}, formal_name="Get Request"))
    return vega
