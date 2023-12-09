from collections import defaultdict
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Style

from ..constants import TEXT

class InvalidUserArgs(Exception):
    pass

class InvalidUserDateType(Exception):
    pass

WEEKDAYS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
LAST_WORK_DAY = 4 # Friday
DAYS_RANGE = 7

def get_weekday(weekday):
    """Takes the number of the week and returns the name of the week day or Monday if the weekday falls on a weekend
    
    Parameters:
        weekday (int): the number of the week, exp: 0

    Returns:
        str: the name of the week day, exp: Monday
    """
    return WEEKDAYS[0] if weekday > LAST_WORK_DAY else WEEKDAYS[weekday]

def parse_user_data(user):
    """Checks required keys in user data and eirther returns name and birthday values or raise an exception
    
    Parameters:
        user (dict): exp: {"name": "Bill Gates", "birthday": datetime(1955, 11, 11)}

    Returns:
        tuple: exp: (\"Bill Gates\", datetime(1955, 11, 11)) or raise an exception
    """
    if not ("name" in user and "birthday" in user):
        raise InvalidUserArgs

    if not isinstance(user["birthday"], datetime):
        raise InvalidUserDateType
    
    name = user["name"]
    birthday = user["birthday"].date()
    return name, birthday

def get_birthdays_per_week(users, days_range = None):
    """Takes the list of users with required \"name\" and \"birthday\" keys and show them with birthdays one week ahead of the current day

    Parameters:
    users (list(dict)): the list of dicts, exp: [{"name": "Bill Gates", "birthday": datetime(1955, 11, 11)}]

    Output:
    displays birthdays one week ahead of the current day, exp: Monday: Bill Gates
    """
    if days_range is None:
        days_range = DAYS_RANGE

    today = datetime.today().date()
    grouped_birthdays = defaultdict(list)

    for user in users:
        try:
            name, birthday = parse_user_data(user)
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if delta_days < days_range:
                birthday_weekday = birthday_this_year.weekday()
                weekday = get_weekday(birthday_weekday)
                grouped_birthdays[weekday].append(name)
        except InvalidUserArgs:
            print(Fore.RED + "Not found required \"name\" and \"birthday\" keys."+ Style.RESET_ALL)
        except InvalidUserDateType:
            print(Fore.RED + "Birthday value must be a datetime type." + Style.RESET_ALL)
        except Exception as err:
            print(Fore.RED + f"Oops! Something went wrong, {err}" + Style.RESET_ALL)
    

    if len(grouped_birthdays) > 0:
        table = PrettyTable(['Weekday', 'Contacts'])
        table.align = "l"
        table.max_width = 80
        table.min_width = 15

        for weekday, users_list in grouped_birthdays.items():
            table.add_row([
                weekday,
                ", ".join(users_list)
            ])
        print(table)
    else:
        print(TEXT["NO_DATA_TO_DISPLAY"])

__all__ = ["get_birthdays_per_week"]