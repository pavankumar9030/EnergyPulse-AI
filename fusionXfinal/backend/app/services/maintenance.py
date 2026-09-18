from datetime import datetime, timedelta


def get_maintenance_status(last_cleaned_at: str, current_date: str, interval_days: int = 15) -> dict:
    last = datetime.strptime(last_cleaned_at, "%Y-%m-%d")
    today = datetime.strptime(current_date, "%Y-%m-%d")
    next_due = last + timedelta(days=interval_days)
    delta = (today - next_due).days
    if delta > 0:
        status = "Overdue"
    elif (next_due - today).days <= 3:
        status = "Due soon"
    else:
        status = "Due"
    return {"state": status, "last_cleaned_at": last_cleaned_at, "next_cleaning_at": next_due.strftime("%Y-%m-%d")}


def mark_cleaned(record: dict) -> dict:
    last_cleaned = datetime.strptime(record["last_cleaned_at"], "%Y-%m-%d")
    interval = int(record.get("maintenance_interval_days", 15))
    next_cleaning = last_cleaned + timedelta(days=interval)
    record["next_cleaning_at"] = next_cleaning.strftime("%Y-%m-%d")
    return record
