from datetime import datetime, timedelta


def date_range(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates
dates = date_range("2023-04-01", "2023-04-30")
print(f'{dates}')
