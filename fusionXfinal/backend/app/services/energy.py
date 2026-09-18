def calculate_appliance_energy(appliance: dict) -> float:
    power_kw = float(appliance.get("rated_power_kw", 0.0))
    hours = float(appliance.get("usage_hours", appliance.get("usage_hours_per_day", 0.0)))
    quantity = float(appliance.get("quantity", 1))
    return power_kw * hours * quantity


def aggregate_energy(buildings: list[dict]) -> float:
    total = 0.0
    for building in buildings:
        for appliance in building.get("appliances", []):
            total += calculate_appliance_energy(appliance)
    return total


def compute_savings(current_cost: float, percent_saved: float) -> float:
    return current_cost * (percent_saved / 100)
