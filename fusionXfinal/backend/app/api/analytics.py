from fastapi import APIRouter, Depends

from app.api.auth import get_current_user

router = APIRouter()


@router.get("/forecast")
def forecast(building_id: int | None = None, start_date: str | None = None, end_date: str | None = None, zone_id: int | None = None, user=Depends(get_current_user)):
    return {
        "timestamp": "2026-09-18T00:00:00Z",
        "predicted_kwh": 52.4,
        "actual_kwh": 50.8,
        "building_id": building_id,
        "zone_id": zone_id,
        "start_date": start_date,
        "end_date": end_date,
    }


@router.get("/anomalies")
def anomalies(user=Depends(get_current_user)):
    return [{"zone": "Room 203", "appliance": "Air Conditioner", "actual_usage": 61.1, "predicted_usage": 42.2, "risk_level": "High", "explanation": "Energy consumption in Room 203 is 44% above the expected level. The AC is operating during a period of low occupancy."}]


@router.get("/recommendations")
def recommendations(user=Depends(get_current_user)):
    return [{"action": "Raise AC setpoint by 2°C", "zone": "Room 203", "appliance": "Air Conditioner", "estimated_kwh_saved": 8.5, "estimated_cost_saved": 12.75, "effort_score": 2, "priority": 4.25, "reason": "Lower cooling demand during low occupancy."}]


@router.get("/recommendations/lighting")
def lighting_recommendations(user=Depends(get_current_user)):
    return [{"action": "Turn off unnecessary lights during daylight", "zone": "Lobby", "estimated_kwh_saved": 3.0, "reason": "Daylight is available and occupancy is low."}]


@router.get("/weekly-comparison")
def weekly_comparison(user=Depends(get_current_user)):
    return {"current_week": [35, 41, 38, 47, 52, 48, 44], "previous_week": [39, 44, 42, 45, 50, 46, 41]}


@router.get("/day-comparison")
def day_comparison(user=Depends(get_current_user)):
    return {"today": 52.4, "yesterday": 49.5, "percentage_change": 5.86}


@router.get("/benchmark")
def benchmark(user=Depends(get_current_user)):
    return {"energy_per_person": 12.5, "comparisons": [{"label": "Building A", "energy_per_person": 12.5}, {"label": "Building B", "energy_per_person": 10.1}, {"label": "Building C", "energy_per_person": 9.8}]}


@router.post("/simulate")
def simulate(payload: dict, user=Depends(get_current_user)):
    return {"current_demand": 15.0, "simulated_demand": 12.7, "energy_saved": 2.3, "cost_saved": 0.28, "scenario": payload}
