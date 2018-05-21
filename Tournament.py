import time


class Tournament(object):
    """A tournament class to define various structures."""

    def __init__(self, players, type="Double-Up SNG", buyin=10.00, speed="Turbo"):
        self.players = players
        self.type = type
        self.buyin = buyin
        self.speed = speed

    def print_tournament(self):
        print("There are {} players in a {} buy-in {} tournament " \
            "that is a {} speed.".format(self.players, self.buyin,
            self.type, self.speed))

    def create_position_dictionary(self):
        if self.players == 9:
            return {
                    1: "Small Blind",
                    2: "Early Position",
                    3: "Early Position",
                    4: "Middle Position",
                    5: "Middle Position",
                    6: "Middle Position",
                    7: "Late Position",
                    8: "Late Position",
                    9: "Button",
                    }
        elif self.players == 6:
            return {
                    1: "Small Blind",
                    2: "Early Position",
                    3: "Middle Position",
                    4: "Middle Position",
                    5: "Late Position",
                    6: "Button",
                    }


class DoubleUpSngTurbo(Tournament):

    def __init__(self, buyin, fee, players=6):
        self.players = players
        self.buyin = buyin
        self.fee = fee
        self.type = "Double-Up SNG"
        self.start_time = time.time()
        self.blinds = {
            1: (0, 10, 20),
            2: (0, 15, 30),
            3: (0, 25, 50),
            4: (0, 50, 100),
            5: (0, 100, 200),
            6: (0, 150, 300),
            7: (30, 200, 400),
            8: (45, 250, 500),
            9: (50, 500, 1000)
        }

    def get_blind_level(self):
        elapsed_time = round(time.time()-self.start_time, 3)
        if elapsed_time < 300.0:
            blind_level = self.blinds[1]
        elif elapsed_time < 600.0:
            blind_level = self.blinds[2]
        print("Antes are {}, small blind is {}, and big blind is {}.".format(blind_level[0], blind_level[1], blind_level[2]))
        return blind_level

    def calculate_big_blinds_remaining(self, chip_stack):
        big_blinds_remaining = chip_stack/self.get_blind_level()[2]
        print(big_blinds_remaining)



#Module Testing
test = DoubleUpSngTurbo(20.00, 1.00, 6)
time.sleep(5)
#test.get_blind_level()
test.calculate_big_blinds_remaining(1500)






#
