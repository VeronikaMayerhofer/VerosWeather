from datetime import datetime, date, timedelta

# computes the start and end date of a given calendar week

class CalendarWeekService:
    def __init__(self):
        pass

    def compute_start_end_day(self, calendar_week: int) -> tuple[date, date]:
        start_date = date.fromisocalendar(datetime.now().year, calendar_week, 1)
        return start_date, start_date + timedelta(days=6)
