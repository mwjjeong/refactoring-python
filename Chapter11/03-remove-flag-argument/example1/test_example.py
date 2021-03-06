from datetime import datetime

from example import rush_delivery_date, regular_delivery_date
from order import Order


def test_order_ma():
    order = Order("MA", datetime.strptime("01/25/22", "%m/%d/%y"))
    assert rush_delivery_date(order) == datetime.strptime(
        "01/27/22", "%m/%d/%y"
    )
    assert regular_delivery_date(order) == datetime.strptime(
        "01/29/22", "%m/%d/%y"
    )


def test_order_ct():
    order = Order("CT", datetime.strptime("01/25/22", "%m/%d/%y"))
    assert rush_delivery_date(order) == datetime.strptime(
        "01/27/22", "%m/%d/%y"
    )
    assert regular_delivery_date(order) == datetime.strptime(
        "01/29/22", "%m/%d/%y"
    )


def test_order_ny():
    order = Order("NY", datetime.strptime("01/25/22", "%m/%d/%y"))
    assert rush_delivery_date(order) == datetime.strptime(
        "01/28/22", "%m/%d/%y"
    )
    assert regular_delivery_date(order) == datetime.strptime(
        "01/29/22", "%m/%d/%y"
    )


def test_order_me():
    order = Order("ME", datetime.strptime("01/25/22", "%m/%d/%y"))
    assert rush_delivery_date(order) == datetime.strptime(
        "01/29/22", "%m/%d/%y"
    )
    assert regular_delivery_date(order) == datetime.strptime(
        "01/30/22", "%m/%d/%y"
    )


def test_order_nh():
    order = Order("NH", datetime.strptime("01/25/22", "%m/%d/%y"))
    assert rush_delivery_date(order) == datetime.strptime(
        "01/28/22", "%m/%d/%y"
    )
    assert regular_delivery_date(order) == datetime.strptime(
        "01/30/22", "%m/%d/%y"
    )
