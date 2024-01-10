import datetime

import integrations.VegaAPI as api
from time import sleep

ITG_NAME = "Epidemic_S"
event = api.Event("LogIncomingData", outputs={"Hours": int, "Infected": int})


def vega_main():
    vega = api.Vega_Portal()
    vega.set_name(ITG_NAME)
    vega.add_event(event)
    return vega


class Epidemic:
    def __init__(self, init_patients):
        self.init_patients = init_patients
        self.r = 2
        self.init_time = datetime.datetime.now()
        self.time = 0
        self.conn = api.VegaConnection(False)
        self.infections = self.init_patients

    def step(self):
        self.time += 1
        self.infections = self.init_patients * (1 + self.r) ** self.time

    def send_data(self, event, data):
        if self.conn:
            if self.conn.is_closing:
                try:
                    self.conn = api.VegaConnection(False)
                    self.send_data(event, data)
                except:
                    print("Could not connect to Vega Portal.")
            else:
                self.conn.emit(event, data)
        else:
            try:
                self.conn = api.VegaConnection(False)
                self.send_data(event, data)
            except:
                print("Could not connect to Vega Portal.")


if __name__ == "__main__":
    ep = Epidemic(3)
    while True:
        ep.step()
        ep.send_data(event, {"Hours": ep.time, "Infected": ep.infections})
        sleep(3)