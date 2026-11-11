import pandas as pd
import os
import json

# main function
def process_matches(career_js, player, birthday):
    player_df = 

# helper functions
def get_matches(career_js):
    matches = get_js_data(career_js)

def get_opp_age(val, match_date):

def get_js_data(career_js, var):
    _, found, after = career_js.partition(var)


cwd = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(cwd)
PATH_TO_DATA = os.path.join(project_root, "data")

serena_js_path = os.path.join(PATH_TO_DATA, "SerenaWilliamsCareer.js")

with open (serena_js_path, "r") as file:
    serena_js = file.read()

# for all the matches, removing javascript assignment and semicolon delimiters(?) to load in python lists
matches = json.loads(serena_js.split("=", 1)[1].strip().rstrip(";"))

serena_df = pd.DataFrame(matches)

match_dates = pd.to_datetime(serena_df[0], format="%Y%m%d")
opp_birthday = pd.to_datetime(serena_df[16], format="%Y%m%d")
sw_birthday = pd.Timestamp("1981-09-26")

serena = pd.DataFrame({
    "Match Date": match_dates,
    "Opponent": serena_df[11],
    "Williams Age": (match_dates - sw_birthday).dt.days / (365 + 0.25),
    "Opponent Age": (match_dates - opp_birthday).dt.days / (365 + 0.25),
    "Williams Won": serena_df[4] == "W",
})

serena.to_csv(os.path.join(PATH_TO_DATA, "serena.csv"), index=False)