import datetime as dt
tic = dt.datetime.now()
from zoneinfo import ZoneInfo
import os
import yaml, json
from jinja2 import Environment, FileSystemLoader
import utils

LOOKUP_FOLDER = "lookup"
SETTINGS_FILEPATH = "settings.yaml"
INDEX_TEMPLATE = "template_index.html"
ARTLINKS_TEMPLATE = "template_artlinks.html"
INDEX_FILEPATH = "index.html"
ARTLINKS_FILEPATH = "artlinks.html"
TEMPLE_DAY = 0
TEMPLE_WEEK = 0
TEMPLE_CLOSURES = []
TEMPLE_DAY_MESSAGE = ""
ARTLINKS = {}
CLEANING = {}
MEETING_TYPES = {}
HYMNS = {}
SETTINGS = {} # Used as a data source for the Index page template rendering
SUNDAY_TYPE = None # Upcoming meeting type
SUNDAY_DATE = "" # Ordinal sunday date

def load_artlinks(json_file_path):
    # Simple json to python structure load
    global ARTLINKS
    with open(json_file_path, 'r') as file:
        ARTLINKS = json.load(file)

def load_hymns(json_file_path):
    # Simple json to python structure load
    global HYMNS
    with open(json_file_path, 'r') as file:
        HYMNS = json.load(file)

def load_cleaning(json_file_path):
    """
    Load cleaning assignments from a JSON file, convert date strings to `datetime.date` objects, 
    and populate the global `CLEANING` dictionary with these assignments.

    The JSON file is expected to contain dates as keys (formatted as "DD Month YYYY") 
    and cleaning assignments as string.

    Args:
        json_file_path (str): The file path to the JSON file containing cleaning assignments.

    Returns:
        None: The function updates the global `CLEANING` dictionary.

    Raises:
        FileNotFoundError: If the provided file path does not exist.
        json.JSONDecodeError: If the JSON file contains invalid JSON.
        ValueError: If a date string in the JSON file does not match the expected format.

    Side Effects:
        Updates the global `CLEANING` dictionary with `datetime.date` objects as keys 
        and cleaning assignment strings as values.
    """
    global CLEANING

    # Set format to parse the JSON dates. Default: "5 November 2022"
    date_format = "%d %B %Y"
    # Get current year
    today = dt.date.today()
    current_year = today.year

    with open(json_file_path, 'r') as file:
        jfile = json.load(file)

        for date_str, cleaning_assignment in jfile.items():
            date_obj = dt.datetime.strptime(date_str, date_format).date()
            CLEANING[date_obj] = cleaning_assignment

def load_meeting_types(json_file_path):
    # Simple json to python structure load
    global MEETING_TYPES
    with open(json_file_path, 'r') as file:
        MEETING_TYPES = json.load(file)

def load_temple_day_schedule(json_file_path):
    """
    Load the temple day schedule, including the target weekday, week of the month, 
    and closure intervals, from a JSON file and populate global variables.

    The JSON file must contain the following keys:
    - `temple_day`: Name of the target weekday (e.g., "Sunday", "Saturday").
    - `temple_week`: Week number in the month (e.g., 1 for the first week, 3 for the third week).
    - `temple_closures`: A list of closure periods, each with a `start` and `end` date in the format "DD Month YYYY".

    Args:
        json_file_path (str): The file path to the JSON file containing the temple schedule.

    Returns:
        None: The function updates the global variables:
            - `TEMPLE_DAY` (int): Numeric representation of the target weekday (0 for Monday, 6 for Sunday).
            - `TEMPLE_WEEK` (int): The week of the month.
            - `TEMPLE_CLOSURES` (list of tuple): List of closure intervals as tuples of `datetime.date` objects.

    Raises:
        FileNotFoundError: If the JSON file is not found.
        json.JSONDecodeError: If the JSON file contains invalid JSON.
        ValueError: If the `temple_day`, `temple_week`, or `temple_closures` fields are invalid.

    Side Effects:
        Updates the global variables `TEMPLE_DAY`, `TEMPLE_WEEK`, and `TEMPLE_CLOSURES`.
    """
    global TEMPLE_DAY, TEMPLE_WEEK, TEMPLE_CLOSURES

    with open(json_file_path, 'r') as file:
        # Load the json file
        jfile = json.load(file)
        # Convert weekday name to a constant number
        tday = jfile.get("temple_day", 0)
        TEMPLE_DAY = utils.weekday_to_int(tday)
        # Load the week of the month number
        TEMPLE_WEEK = int(jfile.get("temple_week", 0))
        # Load closures list
        closures = jfile.get("temple_closures", [])
        # Convert closures from strings to dates
        for closure in closures:
            start_date = dt.datetime.strptime(closure["start"], "%d %B %Y").date()
            end_date = dt.datetime.strptime(closure["end"], "%d %B %Y").date()
            TEMPLE_CLOSURES.append((start_date, end_date))

def load_settings(yaml_file_path):
    # Simple json to python structure load
    global SETTINGS
    with open(yaml_file_path, 'r') as yaml_file:
        SETTINGS = yaml.safe_load(yaml_file)

def lookup_hymns():
    """
    Updates hymn information in the global `SETTINGS` dictionary by pulling the hymn title and URL 
    from the global `HYMNS` dictionary based on hymn numbers. HYMNS dictionary previously was loaded from the JSON file.

    The updated information is stored back in `SETTINGS["hymns"]` and ready for HTML rendering template.

    Global Variables:
        SETTINGS (dict): A dictionary containing hymn-related configuration, including:
            - "hymns": A list of hymn entries where each entry is a dictionary with "number" key.
              This is updated with "title" and "url" fields for each hymn.
        HYMNS (dict): A dictionary mapping hymn numbers (as strings) to `[title, URL]`.

    Modifications:
        Updates each hymn entry in `SETTINGS["hymns"]` to include:
        - `title`: The title of the hymn (retrieved from `HYMNS`).
        - `url`: The URL of the hymn (retrieved from `HYMNS`).
    Args:
        None

    Returns:
        None: This function updates the `SETTINGS` dictionary in place.

    Raises:
        KeyError: If required keys are missing in `SETTINGS["hymns"]` or `HYMNS`.
        AttributeError: If `SETTINGS["hymns"]` is not a dictionary or does not contain valid hymn entries.

    """
    global SETTINGS
    for hymn in SETTINGS.get("hymns", []).values():
        number = hymn["number"]
        hymn["title"] = HYMNS.get(str(number), ["", ""])[0]
        hymn["url"] = HYMNS.get(str(number), ["", ""])[1]

def lookup_cover_image():
    """
    Updates the `SETTINGS` dictionary with a cover image URL.

    This function retrieves the hymn image ID from `SETTINGS["meeting_cover_img"]`, uses this ID to look up 
    the corresponding cover image URL from the `ARTLINKS` dictionary, and stores the result in `SETTINGS["meeting_cover_img_url"]`.

    If the image ID is not found in the `ARTLINKS` dictionary, the URL is set to "NOT FOUND".

    Global Variables:
        SETTINGS (dict): A dictionary containing data for the HTML template rendeing loaded from the settings.yaml, including the key "meeting_cover_img" 
        ARTLINKS (dict): A dictionary mapping image IDs (as strings) to cover image URLs.

    Modifications:
        Updates `SETTINGS["meeting_cover_img_url"]` with the URL corresponding to the image ID from `ARTLINKS`.

    Args:
        None

    Returns:
        None: The function updates `SETTINGS` in place with the corresponding cover image URL.

    Raises:
        KeyError: If `SETTINGS` does not contain the key `"meeting_cover_img"`.
    """
    global SETTINGS
    # Load additional hymn details to the settings variable
    hymn_details = []
    img_id = SETTINGS.get("meeting_cover_img", 0)
    SETTINGS["meeting_cover_img_url"] = ARTLINKS.get(str(img_id), "NOT FOUND")

def set_meeting_type_and_date():
    """
    Determines and sets the meeting type and date for the upcoming Sunday.

    This function retrieves the nearest upcoming Sunday date using the utility function `utils.get_nearest_sunday()`, 
    formats it into a human-readable ordinal date format (e.g., "December 01st") using `utils.format_date_ordinal()`,
    and assigns it to the global variable `SUNDAY_DATE`. It also attempts to find the corresponding meeting type 
    for that date from the `MEETING_TYPES` dictionary and assigns it to `SUNDAY_TYPE`.

    The function updates the global `SETTINGS` dictionary with:
        - `"date"`: The formatted ordinal date for the nearest Sunday.
        - `"meeting_type"`: The corresponding meeting type for that Sunday, if found.

    Global Variables:
        SUNDAY_TYPE (str or None): The meeting type for the nearest Sunday.
        SUNDAY_DATE (str): The ordinal date of the nearest Sunday in the format "Month Day".
        SETTINGS (dict): A dictionary containing configuration settings, which is updated with the keys `"date"` 
                         and `"meeting_type"`.
        MEETING_TYPES (dict): A dictionary that maps formatted Sunday dates (e.g., "December 01") to meeting types.

    Args:
        None

    Returns:
        None: The function modifies global variables `SUNDAY_TYPE`, `SUNDAY_DATE`, and the `SETTINGS` dictionary.

    Raises:
        None
    """
    # Choose which meeting type is it. Set ordinal date format
    global SUNDAY_TYPE, SUNDAY_DATE, SETTINGS
    nearest_sunday = utils.get_nearest_sunday()
    str_date = nearest_sunday.strftime("%B %d") # Format: 'December 01'
    SUNDAY_TYPE = MEETING_TYPES.get(str_date, None)
    SUNDAY_DATE = utils.format_date_ordinal(nearest_sunday)
    
    SETTINGS["date"] = SUNDAY_DATE

    if "meeting_type" not in SETTINGS:
        SETTINGS["meeting_type"] = SUNDAY_TYPE

def load_lookup_files():
    """
    Loads JSON lookup files and prepares most of them for rendering.

    Args:
        None

    Returns:
        None: This function updates the `SETTINGS` dictionary in place.
    """
    load_artlinks(f"{LOOKUP_FOLDER}/artlinks.json")
    #print(ARTLINKS)

    load_cleaning(f"{LOOKUP_FOLDER}/cleaning.json")
    #print(CLEANING)

    load_meeting_types(f"{LOOKUP_FOLDER}/meeting_types.json")

    load_hymns(f"{LOOKUP_FOLDER}/hymns.json")
    #print(HYMNS)

    load_temple_day_schedule(f"{LOOKUP_FOLDER}/temple_day.json")
    #print(TEMPLE_DAY)
    #print(TEMPLE_WEEK)
    #print(TEMPLE_CLOSURES)



def main():

    cwd = os.getcwd()
    print("Current directory is ", cwd)
    load_settings(SETTINGS_FILEPATH)

    load_lookup_files()

    lookup_hymns()

    lookup_cover_image()

    # Get meeting type, unless it's overridden for testing in the settings.yaml
    if "meeting_type" not in SETTINGS:
       set_meeting_type_and_date()
    
    # Calculate next temple day
    #SETTINGS["next_temple_day_title"] = "Next ward temple day: "
    #SETTINGS["next_temple_day"] = utils.next_temple_day(TEMPLE_DAY, TEMPLE_WEEK, TEMPLE_CLOSURES)

    SETTINGS["next_temple_day_title"] = "Upcoming ward temple days: "
    SETTINGS["next_temple_day"] = utils.upcoming_temple_days(TEMPLE_DAY, TEMPLE_WEEK, TEMPLE_CLOSURES, 6)

    # Calculate cleaning schedule (N saturdays from today)
    SETTINGS["next_cleaning_assignments"] = utils.get_nearest_saturday_cleaning(CLEANING, 3)
    #print(SETTINGS["next_cleaning_assignments"])

    # RENDER INDEX.HTML
    # Set up Jinja2 environment and load the HTML template
    env = Environment(loader=FileSystemLoader(searchpath=os.path.dirname(INDEX_TEMPLATE)))
    template = env.get_template(os.path.basename(INDEX_TEMPLATE))
    # Set "last modified" datetime
    central_time = dt.datetime.now(tz=ZoneInfo("America/Chicago"))
    template.globals['now'] = central_time.strftime("%Y-%m-%d %H:%M:%S")

    rendered_html = template.render(SETTINGS)
    # Write the rendered HTML to a file
    with open(INDEX_FILEPATH, "w") as output_file:
        output_file.write(rendered_html)

    
    # RENDER ARTLINKS.HTML
    env = Environment(loader=FileSystemLoader(searchpath=os.path.dirname(ARTLINKS_TEMPLATE)))
    template = env.get_template(os.path.basename(ARTLINKS_TEMPLATE))
    # Set "last modified" datetime
    central_time = dt.datetime.now(tz=ZoneInfo("America/Chicago"))
    template.globals['now'] = central_time.strftime("%Y-%m-%d %H:%M:%S")

    rendered_html = template.render( {
        "artlinks": ARTLINKS
        })
    # Write the rendered HTML to a file
    with open(ARTLINKS_FILEPATH, "w") as output_file:
        output_file.write(rendered_html)

toc = dt.datetime.now()
# find difference loop start and end time and display
td = (toc - tic).total_seconds() * 10**3
print(f"Script executed in  : {td:.03f}ms")

if __name__=="__main__":
    main()
    
main()