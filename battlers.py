class Battler(object):
    def __init__(self, hp, base_atk, base_dfn, base_spd):
        self._max_hp   = hp
        self._base_atk = base_atk
        self._base_dfn = base_dfn
        self._base_spd = base_spd

        self._cur_hp = hp

    @property
    def max_hp(self):
        """
        The maximum hit points of this enemy.
        """
        return self._max_hp


    @property
    def cur_hp(self):
        """
        The current hit points of this enemy.
        """
        return self._cur_hp


    @property
    def foo(self):
        return self._foo


    @property
    def atk(self):
        return self._base_atk


    @property
    def dfn(self):
        return self._base_dfn


    @property
    def name(self):
        return self._name


    @property
    def spd(self):
        """
        The frequency with which this entity attacks
        """
        return self._base_spd


    def __str__(self):
        return f"{self.name}[{self.cur_hp}/{self.max_hp},atk={self.atk},def={self.dfn},spd={self.spd}]"


class Bob(Battler):
    def __init__(self):
        super(Bob, self).__init__(hp=5,
                                  base_atk=1,
                                  base_dfn=1,
                                  base_spd=11)

    _name = "Bob"


class Billy(Battler):
    def __init__(self):
        super(Billy, self).__init__(hp=5,
                                    base_atk=3,
                                    base_dfn=1,
                                    base_spd=5)

    _name = "Billy"


class Dan(Battler):
    def __init__(self):
        super(Dan, self).__init__(hp=4,
                                  base_atk=3,
                                  base_dfn=3,
                                  base_spd=4)

    _name = "Dan"

class SlowBob(Battler):
    def __init__(self):
        super(SlowBob, self).__init__(hp=5,
                                      base_atk=1,
                                      base_dfn=1,
                                      base_spd=20)

    _name = "SlowBob"


battler_classes_by_name = {Bob._name.upper()     : Bob,
                           Billy._name.upper()   : Billy,
                           Dan._name.upper()     : Dan,
                           SlowBob._name.upper() : SlowBob}

class Human(Battler):
    def __init__(self):
        super(Human, self).__init__(hp=10,
                                    base_atk=2,
                                    base_dfn=0,
                                    base_spd=10)
        self._weapon    = None
        self._shield    = None
        self._all_items = {}

        # NO_COMMIT: restoral
        self._coins = 0

        self._exp = 0
        self._age = 0

    _name = "Human"

    @property
    def weapon(self):
        return self._weapon


    @property
    def all_items(self):
        return self._all_items


    @property
    def shield(self):
        return self._shield


    @property
    def coins(self):
        return self._coins


    @property
    def atk(self):
        weapon = self.weapon
        base_atk = self._base_atk
        if weapon is None:
            return base_atk
        return weapon.atk + base_atk


    @property
    def dfn(self):
        shield = self.shield
        base_dfn = self._base_dfn
        if shield is None:
            return base_dfn
        return shield.dfn + base_dfn


    def train(self, duration):
        self._age += duration
        # NO_COMMIT: incomplete


    def rest(self, duration):
        self._age += duration
        self._cur_hp = min(self.max_hp, self._cur_hp + duration - 1)


    def __str__(self):
        battler_str = super(Human, self).__str__()
        return f"{battler_str} with ${self.coins}"


    def stats_str(self):
        return f"{self}\n  Weapon: {self.weapon}\n  Shield: {self.shield}"




