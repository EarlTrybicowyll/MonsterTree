from battlers import battler_classes_by_name
from shop import Shop

class Level(object):
    def __init__(self, name, enemies, reward, shop_items):
        self._name    = name
        self._enemies = [battler_classes_by_name[e]() for e in enemies]
        self._reward  = reward
        self._shop    = Shop(shop_items)

    @property
    def reward(self):
        return self._reward


    @property
    def enemies(self):
        return self._enemies


    @property
    def score(self):
        """
        The score for beating this level.
        """
        # Score is the minimum number of hp points needed by the player
        # to guarantee a win in this fight (i.e. can only do 1 damage
        # per attack).
        return int(sum(e.max_hp * e.atk * e.spd / e.spd for e in self.enemies))


    @property
    def name(self):
        return self._name


    @property
    def shop(self):
        return self._shop


    @property
    def preview_str(self):
        """
        Returns a string containing the information available to a human when
        previewing the level.
        """
        return (f"{self.name}: {', '.join(str(e) for e in self.enemies)} "
                f"for ${self.reward} and score {self.score}")


def level_data():
    return [Level("Level1", ["BOB"], 4, ["Thumbtack", "Paperback"]),
            Level("Level2", ["BOB", "BOB"], 5, ["ButterKnife", "Paperback"]),
            Level("Level3", ["BILLY"], 7, ["ButterKnife", "Paperback", "Lid"]),
            Level("Level4", ["DAN"], 7, ["ButterKnife", "Lid"]),
            Level("Level5", ["SLOWBOB", "SLOWBOB", "SLOWBOB", "SLOWBOB", "SLOWBOB"], 8, [])]
