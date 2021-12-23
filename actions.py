class Action(object):
    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name


class BuyAction(Action):
    def __init__(self, item_name):
        super(BuyAction, self).__init__("Buy")
        self._item_name = item_name

    @property
    def item_name(self):
        return self._item_name


class StartLevelAction(Action):
    pass


class DisplayStatsAction(Action):
    pass


class PreviewLevelAction(Action):
    pass


class TrainAction(Action):
    def __init__(self, duration):
        super(TrainAction, self).__init__("Train")
        self._duration = int(duration)

    @property
    def duration(self):
        return self._duration


class RestAction(Action):
    def __init__(self, duration):
        super(RestAction, self).__init__("Rest")
        self._duration = int(duration)

    @property
    def duration(self):
        return self._duration
