from datetime import datetime, timezone


def get_utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0)

def generate_time_id() -> int:
    return int(datetime.now().strftime("%Y%m%d%H%M%S"))
