def compute_priority(estimated_kwh_saved: float, effort_score: float) -> float:
    if effort_score == 0:
        return 0.0
    return estimated_kwh_saved / effort_score


def build_recommendations(raw_recommendations: list[dict]) -> list[dict]:
    result = []
    for item in raw_recommendations:
        priority = compute_priority(float(item.get("estimated_kwh_saved", 0)), float(item.get("effort_score", 1)))
        result.append({**item, "priority": priority})
    return sorted(result, key=lambda x: x["priority"], reverse=True)
