from adjustment import Adjustment
from production_plan import ProductionPlan
from production_plan2 import ProductionPlan as ProductionPlan2


def test_production():
    production_plan = ProductionPlan()
    production_plan.apply_adjustment(Adjustment(100))
    production_plan.apply_adjustment(Adjustment(250))
    production_plan.apply_adjustment(Adjustment(300))
    assert production_plan.production == 650


def test_production2():
    production_plan = ProductionPlan2(200)
    production_plan.apply_adjustment(Adjustment(100))
    production_plan.apply_adjustment(Adjustment(250))
    production_plan.apply_adjustment(Adjustment(300))
    assert production_plan.production == 850
