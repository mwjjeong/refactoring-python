class Order:
    def __init__(self, base_price):
        self._base_price = base_price

    def is_expensive(self):
        return self._base_price > 1000
