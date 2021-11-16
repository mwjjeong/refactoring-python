import math


def statement(invoice: dict, plays: dict) -> str:
    statement_data = {}
    return render_plain_text(statement_data, invoice, plays)


def render_plain_text(data: dict, invoice: dict, plays: dict) -> str:
    result = f'Invoice (Customer: {invoice["customer"]})\n'

    for perf in invoice["performances"]:
        result += (
            f'\t{get_play_for(perf, plays)["name"]}: '
            f"{get_usd(get_amount_for(perf, plays))} "
            f'({perf["audience"]} Seats)\n'
        )

    result += f"Total Amount: {get_usd(get_total_amount(invoice, plays))}\n"
    result += f"Volume Credits: {get_total_volume_credits(invoice, plays)}\n"
    return result


def get_total_amount(invoice: dict, plays: dict) -> int:
    result = 0
    for perf in invoice["performances"]:
        result += get_amount_for(perf, plays)
    return result


def get_total_volume_credits(invoice: dict, plays: dict) -> int:
    result = 0
    for perf in invoice["performances"]:
        result += get_volume_credits_for(perf, plays)
    return result


def get_usd(num: float) -> str:
    return "${:,.2f}".format(num / 100)


def get_volume_credits_for(performance: dict, plays: dict) -> int:
    result = max(performance["audience"] - 30, 0)
    if get_play_for(performance, plays)["type"] == "comedy":
        result += math.floor(performance["audience"] / 5)

    return result


def get_amount_for(performance: dict, plays: dict) -> int:
    result = 0

    if get_play_for(performance, plays)["type"] == "tragedy":
        result = 40000
        if performance["audience"] > 30:
            result += 1000 * (performance["audience"] - 30)
    elif get_play_for(performance, plays)["type"] == "comedy":
        result = 30000
        if performance["audience"] > 20:
            result += 10000 + 500 * (performance["audience"] - 20)
        result += 300 * performance["audience"]
    else:
        raise ValueError(
            f'Unknown genre: {get_play_for(performance, plays)["type"]}'
        )

    return result


def get_play_for(performance: dict, plays: dict) -> dict:
    return plays[performance["playID"]]
