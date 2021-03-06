class HeatingPlan:
    def __init__(self, min, max) -> None:
        self._min = min
        self._max = max

    def target_temperature(self, selected_temperature):
        if selected_temperature > self._max:
            return self._max
        elif selected_temperature < self._min:
            return self._min
        else:
            return selected_temperature
