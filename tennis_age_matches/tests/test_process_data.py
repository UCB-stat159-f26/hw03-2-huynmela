import os
import pandas as pd
import pytest

from tennis_age_matches.process_data import _find_player, _process_matches

cwd = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(cwd))
PATH_TO_DATA = os.path.join(project_root, "data")

def _get_js(filename):
    with open(os.path.join(PATH_TO_DATA, filename), "r", encoding="utf-8") as file:
        career_js = file.read()
    return career_js

def test_femaleplayercareer():
    # Testing Serena Williams 
    career_js = _get_js("FemalePlayerCareer.js")
    player = _process_matches(career_js, "Serena Williams", "19810926")
    first_match = player.iloc[0]

    assert first_match["Match Date"] == pd.Timestamp("1995-10-30")
    assert first_match["Opponent"] == "Anne Miller"
    assert first_match["Player Age"] == pytest.approx(5147 / 365.25)
    assert first_match["Opponent Age"] == pytest.approx(6858 / 365.25)
    assert player["Player Won"].tolist() == [False, False, False]

def test_maleplayercareer():
    # Testing Rafael Nadal 
    career_js = _get_js("MalePlayerCareer.js")
    player = _process_matches(career_js, "Rafael Nadal", "19860603")
    first_match = player.iloc[0]

    assert first_match["Match Date"] == pd.Timestamp("2001-09-10")
    assert first_match["Opponent"] == "Guillermo Platel"
    assert first_match["Player Age"] == pytest.approx(5578 / 365.25)
    assert first_match["Opponent Age"] == pytest.approx(22.264202601)
    assert player["Player Won"].tolist() == [False, False, True]

def test_naming_format():
    directory_js = 'var playerlist = ["(W) Serena Williams", "(M) Rafael Nadal"];'
    names = ["serena williams", "Serena Williams", "SerenaWilliams"]
    for name in names: 
        assert _find_player(name, directory_js) == ("Serena Williams", "(W)")

def test_unknown_name():
    directory_js = 'var playerlist = ["(W) Serena Williams", "(M) Rafael Nadal"];'
    with pytest.raises(ValueError, match="GastonSanchez"):
        _find_player("GastonSanchez", directory_js)