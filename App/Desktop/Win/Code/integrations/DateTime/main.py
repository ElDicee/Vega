from App.Desktop.Win.Code.integrations import VegaAPI as api
import datetime
import time


def now_date():
    return datetime.datetime.now()


def today_date():
    return datetime.datetime.today()

def vega_main():
    vega = api.Vega_Portal()
    vega.set_name("DateTime")
    vega.add_method(api.Method(now_date, api.OPERATOR, outputs={"Date": None}, formal_name="Now Date"))
    vega.add_method(api.Method(today_date, api.OPERATOR, outputs={"Date": None}, formal_name="Today Date"))
    return vega
