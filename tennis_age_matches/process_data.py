import pandas as pd
import os
import json

# main function
def process_matches(career_js, player_name, birthday):
    player_df = get_matches(career_js)
    match_dates = pd.to_datetime(player_df[0], format="%Y%m%d")
    player_birthday = pd.to_datetime(birthday, format="%Y%m%d")
    
    player = pd.DataFrame({
        "Match Date" : match_dates,
        "Player" : player_name, 
        "Opponent" : player_df[11],
        "Player Age" : (match_dates - player_birthday).dt.days / 365.25,
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