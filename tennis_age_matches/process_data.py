import pandas as pd
import os
import json

# main function
def _process_matches(career_js, player_name, birthday):
    player_df = _get_matches(career_js)
    match_dates = pd.to_datetime(player_df[0], format="%Y%m%d")
    player_birthday = pd.to_datetime(birthday, format="%Y%m%d")
    
    player = pd.DataFrame({
        "Match Date" : match_dates,
        "Player" : player_name, 
        "Opponent" : player_df[11],
        "Player Age" : (match_dates - player_birthday).dt.days / 365.25,
        "Opponent Age" : [_get_opp_age(val, date) for val, date in zip(player_df[16], match_dates)], 
        "Player Won" : player_df[4] == "W"
        })
    return player

# helper functions
def _get_opp_age(val, match_date):
    val = str(val).strip()
    if not (len(val) == 8 and val.isdigit()):
        return pd.to_numeric(val, errors="coerce")
    opp_birthday = pd.to_datetime(val, format="%Y%m%d", errors="coerce")
    age = (match_date - opp_birthday).days / 365.25
    return age

def _get_js_data(career_js, var):
    _, _, after = career_js.partition(var)
    text_array = after.split("=", 1)[1].lstrip()
    vals, _ = json.JSONDecoder().raw_decode(text_array)
    return vals

def _get_matches(career_js):
    matches = _get_js_data(career_js, "morematchmx")
    player_df = pd.DataFrame(matches)
    player_df = player_df[player_df[4].isin(["W", "L"])]
    return player_df.reset_index(drop=True)

def _find_player(player_name, directory_js):
    players = _get_js_data(directory_js, "playerlist")
    name_found = player_name.replace(" ", "").lower() # standardize names
    for val in players: 
        tour, _, name = val.strip().partition(" ")
        if name.replace(" ", "").lower() == name_found: return name.strip(), tour
    raise ValueError(f"{player_name} not found on tennisabstract.com")

def _get_birthday(player_profile):
    player_profile = "".join(player_profile.split())
    for var in ["vardob=", "varbd="]:
        if var in player_profile:
            after = player_profile.split(var, 1)[1].lstrip("'\"")
            birthday = after[:8]
            if len(birthday) == 8 and birthday.isdigit() and birthday != "00000000":
                return birthday