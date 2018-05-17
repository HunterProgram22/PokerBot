class PositionStrategy(object):
    TIER_ONE = ["AA", "KK", "QQ", "JJ", "AK"]
    TIER_TWO = ["TT", "99", "88", "77", "AQ", "AJ"]
    TIER_THREE = ["KQs", "QJs", "JTs"]
    TIER_FOUR = ["66", "55", "44", "33", "22", "109s", "98s"]

    def __init__(self, Tournament):
        self.tournament_position_dict = Tournament.create_position_dictionary()

    def action(self, cards, position):
        self.cards = cards
        if self.tournament_position_dict[position] == "Early Position":
            self.early_position_action()
        elif self.tournament_position_dict[position] == "Middle Position":
            self.middle_position_action()
        elif self.tournament_position_dict[position] == "Late Position":
            self.late_position_action()

    def early_position_action(self):
        if self.cards in PositionStrategy.TIER_ONE:
            print("Raise limper or re-raise any standard bet.")
        elif self.cards in PositionStrategy.TIER_TWO:
            print("Raise limper or call any standard bet.")
        else:
            print("Fold")

    def middle_position_action(self):
        if self.cards in PositionStrategy.TIER_ONE:
            print("Raise if first in, Else raise limper or reraise.")
        elif self.cards in PositionStrategy.TIER_TWO:
            print("Raise if first in, Else call standard raise.")
        elif self.cards in PositionStrategy.TIER_THREE:
            print("Raise if first in, Else call standard raise.")
        else:
            print("Fold")

    def late_position_action(self):
        print("If first in raise,")
        if self.cards in PositionStrategy.TIER_ONE:
            print("Else raise limper or reraise.")
        elif self.cards in PositionStrategy.TIER_TWO:
            print("Else call standard raise.")
        elif self.cards in PositionStrategy.TIER_THREE:
            print("Else call standard raise.")
        elif self.cards in PositionStrategy.TIER_FOUR:
            print("Else call standard raise.")
        else:
            print("Else fold, unless button, then limp in or call standard raise with any two cards.")