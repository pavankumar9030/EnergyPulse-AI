def simulate_ac_setpoint_change(current_demand: float, increase_c: float, hours: float) -> dict:
    reduction_ratio = min(0.32, 0.05 * increase_c)
    simulated_demand = current_demand * (1 - reduction_ratio)
    energy_saved = current_demand - simulated_demand
    return {
        "current_demand": current_demand,
        "simulated_demand": simulated_demand,
        "energy_saved": energy_saved * hours,
        "cost_saved": (energy_saved * hours) * 0.12,
    }
