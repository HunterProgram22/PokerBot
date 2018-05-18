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
