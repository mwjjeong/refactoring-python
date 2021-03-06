def distance_travelled(scenario, time):
    primary_acceleration = scenario.primary_force / scenario.mass  # a = F / m
    primary_time = min(time, scenario.delay)
    result = 0.5 * primary_acceleration * primary_time * primary_time
    secondary_time = time - scenario.delay
    if secondary_time > 0:
        primary_velocity = primary_acceleration * scenario.delay
        secondary_acceleration = (
            scenario.primary_force + scenario.secondary_force
        ) / scenario.mass
        result += (
            primary_velocity * secondary_time
            + 0.5 * secondary_acceleration * secondary_time * secondary_time
        )
    return result


def discount(input_value, quantity):
    result = input_value
    if result > 50:
        result = result - 2
    if quantity > 100:
        result = result - 1
    return result
