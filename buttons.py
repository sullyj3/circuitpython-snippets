from adafruit_circuitplayground import cp

ALL_BUTTONS = ["A1", "A2", "A3", "A4", "A5", "A6", "TX", "BTN_A", "BTN_B"]

'''Track when buttons are pressed and released

This is a substitute for an event system. Keeps track of when buttons are pressed or released.
You don't need this to know if the buttons are currently down, that's what cp.touch_A1 etc are for.

usage:

    buttons = Buttons()
    while True:
        buttons.update()
        if buttons.pressed["A1"]:
            # handle a1 pressed

        if buttons.released["A1"]:
            # handle a1 released
'''
class Buttons:
    def __init__(self):
        # prev essentially tracks the down state of each button, lagging by one
        # update call.
        # So for example, if a button was `up` last update call, but is `down`
        # now, that means the button must have been pressed in the intervening time
        self.prev = {
            "A1": cp.touch_A1,
            "A2": cp.touch_A2,
            "A3": cp.touch_A3,
            "A4": cp.touch_A4,
            "A5": cp.touch_A5,
            "A6": cp.touch_A6,
            "TX": cp.touch_TX,
            "BTN_A" : cp.button_a,
            "BTN_B" : cp.button_b
            }

        self.pressed = {b:False for b in ALL_BUTTONS}
        self.released = {b:False for b in ALL_BUTTONS}

    # Determine which buttons were pressed or released in the time since the last update call
    # sets the state of self.pressed or self.released, which are then available for inspection
    def update(self):
        # Clear the events that happened last time
        for b in self.pressed:
            self.pressed[b] = False
        for b in self.released:
            self.released[b] = False

        # check whether each button was pressed or released since last time
        if not self.prev["A1"] and cp.touch_A1:
            self.pressed["A1"] = True
            self.prev["A1"] = True
        elif self.prev["A1"] and not cp.touch_A1:
            self.released["A1"] = True
            self.prev["A1"] = False

        if not self.prev["A2"] and cp.touch_A2:
            self.pressed["A2"] = True
            self.prev["A2"] = True
        elif self.prev["A2"] and not cp.touch_A2:
            self.released["A2"] = True
            self.prev["A2"] = False

        if not self.prev["A3"] and cp.touch_A3:
            self.pressed["A3"] = True
            self.prev["A3"] = True
        elif self.prev["A3"] and not cp.touch_A3:
            self.released["A3"] = True
            self.prev["A3"] = False

        if not self.prev["A4"] and cp.touch_A4:
            self.pressed["A4"] = True
            self.prev["A4"] = True
        elif self.prev["A4"] and not cp.touch_A4:
            self.released["A4"] = True
            self.prev["A4"] = False

        if not self.prev["A5"] and cp.touch_A5:
            self.pressed["A5"] = True
            self.prev["A5"] = True
        elif self.prev["A5"] and not cp.touch_A5:
            self.released["A5"] = True
            self.prev["A5"] = False

        if not self.prev["A6"] and cp.touch_A6:
            self.pressed["A6"] = True
            self.prev["A6"] = True
        elif self.prev["A6"] and not cp.touch_A6:
            self.released["A6"] = True
            self.prev["A6"] = False

        if not self.prev["TX"] and cp.touch_TX:
            self.pressed["TX"] = True
            self.prev["TX"] = True
        elif self.prev["TX"] and not cp.touch_TX:
            self.released["TX"] = True
            self.prev["TX"] = False

        if not self.prev["BTN_A"] and cp.button_a:
            self.pressed["BTN_A"] = True
            self.prev["BTN_A"] = True
        elif self.prev["BTN_A"] and not cp.button_a:
            self.released["BTN_A"] = True
            self.prev["BTN_A"] = False

        if not self.prev["BTN_B"] and cp.button_b:
            self.pressed["BTN_B"] = True
            self.prev["BTN_B"] = True
        elif self.prev["BTN_B"] and not cp.button_b:
            self.released["BTN_B"] = True
            self.prev["BTN_B"] = False

