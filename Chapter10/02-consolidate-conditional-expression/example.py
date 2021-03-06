def disability_amount(employee):
    if is_not_eligible_for_disability(employee):
        return 0
    return 1


def vacation_amount(employee):
    if employee.on_vacation and employee.seniority > 10:
        return 1
    return 0.5


def is_not_eligible_for_disability(employee):
    return (
        employee.seniority < 2
        or employee.months_disabled > 12
        or employee.is_part_time
    )
