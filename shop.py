class Item(object):
    def __init__(self, name, cost, description):
        self._name = name
        self._cost = cost
        self._description = description

    @property
    def name(self):
        return self._name


    @property
    def description(self):
        return self._description


    @property
    def cost(self):
        return self._cost


    def apply(self, player):
        player._all_items[self.name.upper()] = self


class Weapon(Item):
    def __init__(self, name, cost, description, atk):
        super(Weapon, self).__init__(name, cost, description)
        self._atk = atk


    @property
    def atk(self):
        return self._atk


    def apply(self, player):
        super(Weapon, self).apply(player)
        player._weapon = self


    def __str__(self):
        return f"{self.name}(+{self.atk}atk)"


class Shield(Item):
    def __init__(self, name, cost, description, dfn):
        super(Shield, self).__init__(name, cost, description)
        self._dfn = dfn


    @property
    def dfn(self):
        return self._dfn


    def apply(self, player):
        super(Shield, self).apply(player)
        player._shield = self


    def __str__(self):
        return f"{self.name}(+{self.dfn}def)"


thumbtack = Weapon("Thumbtack",
                   cost=2,
                   description="It's kind of pointy, but a bit low range",
                   atk=1)

butter_knife = Weapon("ButterKnife",
                      cost=4,
                      description="Cuts right through butter!",
                      atk=2) # NO_COMMIT: make butter be an enemy

paperback = Shield("Paperback",
                   cost=4,
                   description="Quite the page-turner, if you could take a break",
                   dfn=1)

lid = Shield("Lid",
             cost=8,
             description="Keeps the heat in and enemies slightly further away",
             dfn=2)


all_items = [thumbtack, butter_knife, paperback, lid]
items_by_name = {i.name.upper() : i for i in all_items}


class Shop(object):
    """
    Contains data about what items a player can purchase.
    """
    def __init__(self, items):
        self._items = [items_by_name[i.upper()] for i in items]
        self._items_by_name = {i.name.upper() : i for i in self._items}


    @property
    def items(self):
        return self._items


    @property
    def items_by_name(self):
        return self._items_by_name


    def purchase_item(self, player, item_name):
        item_name = item_name.upper()
        if item_name not in self.items_by_name:
            raise InvalidShopActionError(f"{item_name} not available in {self}")

        if item_name in player.all_items:
            raise InvalidShopActionError(f"You already bought {item_name}")

        item = self.items_by_name[item_name]
        coins = player.coins
        if item.cost > coins:
            raise InvalidShopActionError(f"{item_name} costs {item.cost}, "
                                         f"but you only have {coins}.")

        player._coins -= item.cost

        item.apply(player)


    def __str__(self):
        item_strs = [f'{i}=${i.cost}' for i in self.items]
        return f"Shop: {' '.join(item_strs)}"


class InvalidShopActionError(Exception):
    pass
