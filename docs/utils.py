import datetime as dt
from dateutil.rrule import rrule, MONTHLY, WEEKLY, SU, MO, TU, WE, TH, FR, SA
import calendar


def get_nearest_saturday_cleaning(cleaning_list, n=4):
    """
    Find the next N Saturdays and their corresponding cleaning assignments.

    Args:
        cleaning_list (dict): A dictionary where keys are `datetime.date` objects
            representing cleaning dates, and values are strings of cleaning assignments.
        n (int, optional): The number of upcoming Saturdays to find. Defaults to 4.

    Returns:
        list[dict]: A list of dictionaries, each containing:
            - 'date' (str): The formatted date of the Saturday in "DD Month YYYY" format. Example: '30 November 2024'
            - 'assignment' (str): The cleaning assignment for that Saturday.
        
        Example:
        [
            {'date': '30 November 2024', 'assignment': 'Name1, Name2'},
            {'date': '14 December 2024', 'assignment': 'Name3, Name4'}
        ]
    """
    # Get today's date
    today = dt.date.today()

    # Find the next N Saturdays starting from today
    upcoming_saturdays = list(rrule(freq=WEEKLY, byweekday=SA, count=n, dtstart=today))

    # Match Saturdays with assignments
    results = []
    for saturday in upcoming_saturdays:
        assignment = cleaning_list.get(saturday.date(), None)
        if assignment:
            results.append( 
                {"date": saturday.date().strftime("%d %B %Y"), 
                 "assignment": assignment}
            )

    return results

def get_nearest_sunday():
    """
    Find the closest upcoming Sunday date, including today if it's already Sunday.

    Returns:
        datetime.date: The closest upcoming Sunday as a `datetime.date` object.
        
        If today is Sunday, returns today's date.
        Otherwise, calculates and returns the date of the next Sunday.
        
    Example:
        If today is Friday, November 24, 2024, returns datetime.date(2024, 11, 26)
    """
    today = dt.date.today()
    daynum = today.weekday()  # Sunday is day #6
    
    if daynum == 6:
        return today
    else:
        next_sunday_date = today + dt.timedelta(6 - daynum)
        return next_sunday_date

def str_to_date(_var):
    """
    Convert a string representation of a date into a `datetime.date` object.

    Args:
        _var (str): A string representing a date in the format "DD Month YYYY".

    Returns:
        datetime.date: The corresponding `datetime.date` object.
        
    Raises:
        ValueError: If the input string does not match the expected format.

    Example:
        27 November 2024" -> datetime.date(2024, 11, 27)
        ```
    """
    # Convert string format "27 November 2024" to a datetime.date object
    return dt.datetime.strptime(_var, "%d %B, %Y").date()

def format_date_ordinal(_date):
    """
    Format a date object as a string with an ordinal suffix (e.g., "March 17th" or "January 21st").

    Args:
        _date (datetime.date): A `datetime.date` object representing the date to format.

    Returns:
        str: The formatted date string with an ordinal suffix in the format "Month DDth/st/nd/rd".

    Example:
        date(2024, 3, 17) -> "March 17th"
        date(2024, 11, 22) -> "November 22nd"
    """
    day = _date.day
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    formatted_date = _date.strftime(f"%B {day}{suffix}")
    return formatted_date

def weekday_to_int(target_weekday):
    """
    Convert a weekday name to its corresponding `dateutil.rrule` weekday constant.

    Args:
        target_weekday (str): The name of the weekday (case-insensitive).
            Valid values: "monday", "tuesday", "wednesday", "thursday", 
            "friday", "saturday", "sunday".

    Returns:
        dateutil.rrule.weekday: The `dateutil.rrule` constant corresponding to the weekday.

    Raises:
        KeyError: If the input is not a valid weekday name.

    Example:
        weekday_to_int("Monday") -> dateutil.rrule.MO
    """
    weekday_map = {
        "monday": MO,
        "tuesday": TU,
        "wednesday": WE,
        "thursday": TH,
        "friday": FR,
        "saturday": SA,
        "sunday": SU
    }
    res = weekday_map[str(target_weekday).lower()]
    return res

def next_temple_day(target_weekday, target_week_of_month, closures_list):
    """
    Calculate the next temple day based on the specified weekday, week of the month, and closure intervals.

    Args:
        target_weekday (dateutil.rrule.weekday): The target weekday (e.g., `dateutil.rrule.SA` for Saturday).
        target_week_of_month (int): The week of the month (e.g., 1 for the first week, 3 for the third week).
        closures_list (list of tuple): A list of date ranges representing closure intervals.
            Each tuple contains two `datetime.date` objects (start, end) representing the closed period.
            If the temple is closed for one day, start and end have the same value.

    Returns:
        str: The next open temple day in the format "DD Month YYYY".

    Raises:
        ValueError: If no valid open date is found.
    """

    # Get today's date
    today = dt.date.today()

    # Find the next eligible date (Month on week target_week_of_month on day target_weekday)
    for date in rrule(
        freq=MONTHLY, 
        byweekday=target_weekday, 
        bysetpos=target_week_of_month,
        dtstart=today
    ):
        # Convert the date to datetime.date
        date = date.date()

        # Skip if the date falls within any closure range
        if any(start <= date <= end for start, end in closures_list):
            continue 

        # Return the first valid open date
        return date.strftime("%d %B %Y")

    # If no date is found (unlikely with this logic), return None or raise an error
    raise ValueError("No valid open date found.")

def upcoming_temple_days(target_weekday, target_week_of_month, closures_list, n=6):
    """
    Calculate the next n temple daya based on the specified weekday, week of the month, and closure intervals.

    Args:
        target_weekday (dateutil.rrule.weekday): The target weekday (e.g., `dateutil.rrule.SA` for Saturday).
        target_week_of_month (int): The week of the month (e.g., 1 for the first week, 3 for the third week).
        closures_list (list of tuple): A list of date ranges representing closure intervals.
            Each tuple contains two `datetime.date` objects (start, end) representing the closed period.
            If the temple is closed for one day, start and end have the same value.
        n: Number of dates to return, defaults to 6

    Returns:
        str: a list of upcoming temple days.

    Raises:
        ValueError: If no valid open date is found.
    """

    # Get today's date
    today = dt.date.today()

    # Find the next n eligible dates (Month on week target_week_of_month on day target_weekday)
    result = []
    for date in rrule(
        freq=MONTHLY, 
        byweekday=target_weekday, 
        bysetpos=target_week_of_month, 
        dtstart=today,
        count = n
    ):
        # Convert the date to datetime.date
        date = date.date()

        # Skip if the date falls within any closure range
        if any(start <= date <= end for start, end in closures_list):
            continue 

        # Return the first valid open date
        result.append(date)

    output = ["{0} {1}".format(calendar.month_name[trip.month], trip.day) for trip in result]
    output2 = " " + ", ".join(output)
    return output2
    
    # If no date is found (unlikely with this logic), return None or raise an error

    raise ValueError("No valid open date found.")

#if __name__=="__main__":
  #print(get_nearest_sunday())