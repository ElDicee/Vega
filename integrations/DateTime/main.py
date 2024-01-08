import time
import uuid

import integrations.VegaAPI as api
import datetime
import threading
from time import sleep

ITG_NAME = "DateTime"

event = api.Event("Clock Tick", ITG_NAME, outputs={"Clock ID": str})


def now_date():
    return datetime.datetime.now()


def today_date():
    return datetime.datetime.today()


def get_minute(date):
    return date.minute


def get_second(date):
    return date.second


def get_hour(date):
    return date.hour


def get_day(date):
    return date.day


def get_month(date):
    return date.month


def get_year(date):
    return date.year


def get_weekday(date):
    return date.weekday()


def is_before(date1, date2):
    return date1 < date2


def is_after(date1, date2):
    return date1 > date2


def same_time(date1, date2):
    return date1 == date2


def make_date(year, month, day):
    return datetime.date(year, month, day)


def make_time(hour, minute, second):
    return datetime.time(hour, minute, second)


def combine_date_time(date, time):
    return datetime.datetime.combine(date, time)


class Clock:

    def __init__(self, autostart: bool = False):
        self.init_time = None
        self.uuid = uuid.uuid4()
        self.serv = api.VegaConnection(False)
        self.clock_thread = threading.Thread(target=self.run_clock)
        self.alive = True
        self.tick_rate = 1
        if autostart:
            self.start()

    def __str__(self):
        return self.uuid.__str__()

    def run_clock(self):
        while self.alive:
            self.send_data(event, {"Clock ID": self.uuid.__str__()})
            time.sleep(self.tick_rate)

    def send_data(self, ev, data):
        if self.serv:
            if self.serv.is_closing:
                try:
                    self.serv = api.VegaConnection(False)
                    self.send_data(ev, data)
                except:
                    print("Could not connect to Vega Portal.")
            else:
                self.serv.emit(ev, data)
        else:
            try:
                self.serv = api.VegaConnection(False)
                self.send_data(ev, data)
            except:
                print("Could not connect to Vega Portal.")

    def start(self):
        if not self.init_time:
            self.init_time = datetime.datetime.now()
            self.clock_thread.start()

    def stop(self):
        self.alive = False

    def time_from_init(self):
        if self.init_time:
            return datetime.datetime.now() - self.init_time


def create_clock(autostart: bool):
    return Clock(autostart)


def start_clock(clock):
    clock.start()
    return clock


def time_from_start(clock):
    return clock.time_from_init()


def restart_clock(clock):
    clock.init_time = datetime.datetime.now()
    return clock


def get_clock_id(clock):
    return clock.uuid.__str__()


def set_clock_tick_rate(clock, tickrate: int):
    clock.tick_rate = tickrate
    return clock


def vega_main():
    vega = api.Vega_Portal()
    serv = api.VegaConnection(False)
    vega.set_name("DateTime")
    vega.add_method(api.Method(now_date, api.EXECUTION, outputs={"Date": None}, formal_name="Now Date"))
    vega.add_method(api.Method(today_date, api.OPERATOR, outputs={"Date": None}, formal_name="Today Date"))
    vega.add_method(api.Method(get_second, api.OPERATOR, outputs={"Second": int}, formal_name="Second"))
    vega.add_method(api.Method(get_minute, api.OPERATOR, outputs={"Minute": int}, formal_name="Minute"))
    vega.add_method(api.Method(get_hour, api.OPERATOR, outputs={"Hour": int}, formal_name="Hour"))
    vega.add_method(api.Method(get_day, api.OPERATOR, outputs={"Day": int}, formal_name="Day"))
    vega.add_method(api.Method(get_month, api.OPERATOR, outputs={"Month": int}, formal_name="Month"))
    vega.add_method(api.Method(get_year, api.OPERATOR, outputs={"Year": int}, formal_name="Year"))
    vega.add_method(api.Method(get_weekday, api.OPERATOR, outputs={"Weekday": str}, formal_name="Week Day"))
    vega.add_method(api.Method(is_after, api.OPERATOR, outputs={"Bool": None}, formal_name="Is After"))
    vega.add_method(api.Method(is_before, api.OPERATOR, outputs={"Bool": None}, formal_name="Is Before"))
    vega.add_method(api.Method(same_time, api.OPERATOR, outputs={"Bool": None}, formal_name="Is the Same Time"))
    vega.add_method(api.Method(make_time, api.EXECUTION, outputs={"Time": None}, formal_name="Make Time"))
    vega.add_method(api.Method(make_date, api.EXECUTION, outputs={"Date": None}, formal_name="Make Date"))
    vega.add_method(
        api.Method(combine_date_time, api.OPERATOR, outputs={"Datetime": None}, formal_name="Combine Date Time"))
    vega.add_method(api.Method(create_clock, api.EXECUTION, outputs={"Clock": None}, formal_name="Create Clock"))
    vega.add_method(api.Method(start_clock, api.EXECUTION, outputs={"Clock": None}, formal_name="Start Clock"))
    vega.add_method(api.Method(time_from_start, api.OPERATOR, outputs={"Time"}, formal_name="Clock Time From Start"))
    vega.add_method(api.Method(restart_clock, api.EXECUTION, outputs={"Clock": None}, formal_name="Restart Clock"))
    vega.add_method(api.Method(get_clock_id, api.OPERATOR, outputs={"UUID": str}, formal_name="Clock UUID"))
    vega.add_method(api.Method(set_clock_tick_rate, api.EXECUTION, outputs={"Clock": None}, formal_name="Set Clock Tick Rate"))
    vega.add_event(event)
    return vega
