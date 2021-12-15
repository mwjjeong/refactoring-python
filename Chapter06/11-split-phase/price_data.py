class PriceData:
    def __init__(self, product, quantity) -> None:
        self._product = product
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity
