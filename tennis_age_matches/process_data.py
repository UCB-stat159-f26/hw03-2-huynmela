import pandas as pd
import os
import json

# main function
def process_matches(career_js, player_name, birthday):
    player_df = get_matches(career_js)
    match_dates = pd.to_datetime(player_df[0], format="%Y%m%d")
    player_birthday = pd.to_datetime(birthday, format="%y%m%d")
    
    player = pd.DataFrame({
        "Match Date" : match_dates,
        "Player" : player_name, 
        "Opponent" : player_df[11],
        "Player Age" : (match_dates - player_birthday).dt.days / 365 + 0.25,
        "Opponent Age" : [get_opp_age(val, date) for val, date in zip(player_df[16], match_dates)], 
        "Player Won" : player_df[4] == "W"
        })
    return player

# helper functions
def get_opp_age(val, match_date):
    val = str(val).strip()
    opp_birthday = pd.to_datetime(val, format="%Y%m%d")
    age = (match_date - opp_birthday).days / 365.25
    return age

def get_js_data(career_js, var):
    _, _, after = career_js.partition(var)
    text_array = after.split("=", 1)[1].lstrip()
    vals, _ = json.JSONDecoder().raw_decode(text_array)
    return vals

def get_matches(career_js):
    matches = get_js_data(career_js)
    player_df = pd.DataFrame(matches)
    player_df = player_df[player_df[4].isin(["W", "L"])]
    return player_df.reset_index(drop=True)

# cwd = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.dirname(cwd)
# PATH_TO_DATA = os.path.join(project_root, "data")

# serena_js_path = os.path.join(PATH_TO_DATA, "SerenaWilliamsCareer.js")

# with open (serena_js_path, "r") as file:
    # serena_js = file.read()

# matches = json.loads(serena_js.split("=", 1)[1].strip().rstrip(";"))

# serena_df = pd.DataFrame(matches)

# match_dates = pd.to_datetime(serena_df[0], format="%Y%m%d")
# opp_birthday = pd.to_datetime(serena_df[16], format="%Y%m%d")
# sw_birthday = pd.Timestamp("1981-09-26")

# serena = pd.DataFrame({
#     "Match Date": match_dates,
#     "Opponent": serena_df[11],
#     "Williams Age": (match_dates - sw_birthday).dt.days / (365 + 0.25),
#     "Opponent Age": (match_dates - opp_birthday).dt.days / (365 + 0.25),
#     # "Williams Won": serena_df[4] == "W",
# })

# serena.to_csv(os.path.join(PATH_TO_DATA, "serena.csv"), index=False)