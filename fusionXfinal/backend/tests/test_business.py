from app.services.energy import calculate_appliance_energy, aggregate_energy, compute_savings
from app.services.recommendations import build_recommendations, compute_priority
from app.services.maintenance import get_maintenance_status, mark_cleaned
from app.services.benchmark import calculate_energy_per_person
from app.services.simulation import simulate_ac_setpoint_change


def test_appliance_energy_and_aggregation():
    appliance = {"rated_power_kw": 1.5, "usage_hours": 6, "quantity": 2}
    assert round(calculate_appliance_energy(appliance), 2) == 18.0
    buildings = [{"appliances": [appliance, {"rated_power_kw": 2.0, "usage_hours": 4, "quantity": 1}]}]
    assert round(aggregate_energy(buildings), 2) == 26.0


def test_priority_and_top_recommendations():
    recommendations = [
        {"estimated_kwh_saved": 8, "effort_score": 2},
        {"estimated_kwh_saved": 3, "effort_score": 1},
        {"estimated_kwh_saved": 10, "effort_score": 4},
    ]
    ranked = build_recommendations(recommendations)
    assert ranked[0]["priority"] >= ranked[1]["priority"] >= ranked[2]["priority"]
    assert compute_priority(8, 2) == 4.0


def test_maintenance_due_and_cleaned_update():
    status = get_maintenance_status("2026-01-01", "2026-01-10", 15)
    assert status["state"] == "Due soon"
    record = {"last_cleaned_at": "2026-01-01", "maintenance_interval_days": 15}
    update = mark_cleaned(record)
    assert update["next_cleaning_at"] == "2026-01-16"


def test_benchmark_and_savings():
    assert calculate_energy_per_person(120, 10) == 12.0
    assert compute_savings(100, 20) == 20.0


def test_ac_setpoint_simulation():
    outcome = simulate_ac_setpoint_change(15.0, 2, 6)
    assert outcome["simulated_demand"] < outcome["current_demand"]
    assert outcome["energy_saved"] > 0
