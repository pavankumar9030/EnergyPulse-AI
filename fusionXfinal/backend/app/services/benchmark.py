def calculate_energy_per_person(total_energy_kwh: float, occupants: int) -> float:
    if occupants <= 0:
        return 0.0
    return total_energy_kwh / occupants
