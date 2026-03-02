from datetime import datetime

def parse_date(date_str):
    # BUG: no error handling for invalid format
    return datetime.strptime(date_str, "%Y-%m-%d")

def days_between(date1_str, date2_str):
    d1 = parse_date(date1_str)
    d2 = parse_date(date2_str)
    # BUG: returns negative if date1 > date2
    return (d2 - d1).days

def is_weekend(date_str):
    d = parse_date(date_str)
    # 5=Saturday, 6=Sunday
    return d.weekday() >= 5

def format_date(dt, fmt="%Y/%m/%d"):
    # BUG: crashes if dt is None
    return dt.strftime(fmt)
