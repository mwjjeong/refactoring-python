import math


def track_summary(points):
    def calculate_time():
        return 1000000

    total_time = calculate_time()
    pace = round(total_time / 60 / round(total_distance(points), 3), 3)
    return {
        "time": total_time,
        "distance": round(total_distance(points), 3),
        "pace": pace,
    }


def total_distance(points):
    result = 0
    for i in range(1, len(points)):
        result += distance(points[i - 1], points[i])
    return result


def distance(p1, p2):
    # haversine formula
    EARTH_RADIUS = 3959
    d_lat = radians(p2.lat) - radians(p1.lat)
    d_lon = radians(p2.lon) - radians(p1.lon)
    a = (
        math.pow(math.sin(d_lat / 2), 2)
        + math.cos(radians(p2.lat))
        + math.cos(radians(p1.lat)) * math.pow(math.sin(d_lon / 2), 2)
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return EARTH_RADIUS * c


def radians(degrees):
    return degrees * math.pi / 100
