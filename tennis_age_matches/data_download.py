import requests
from .process_data import _process_matches, _find_player, _get_birthday

tennis_url = "https://www.tennisabstract.com"

def _download_files(files):
    downloaded_files = {}
    for filename, url in files.items():
        get_request = requests.get(url)
        get_request.raise_for_status()
        downloaded_files[filename] = get_request.text
    return downloaded_files
    
def get_player_matches(player_name):
    player_dict = {
        "players" : f"{tennis_url}/mwplayerlist.js"
	}
    directory = _download_files(player_dict)
    name, tour = _find_player(player_name, directory["players"])
    player_id = "".join(letter for letter in name if letter.isalnum())
    player_profile = "wplayer.cgi" if tour == "(W)" else "player.cgi"
	
    files = {
        "career" : f"{tennis_url}/jsmatches/{player_id}Career.js",
        "profile" : f"{tennis_url}/cgi-bin/{player_profile}?p={player_id}"
	}

    downloaded_files = _download_files(files)
    birthday = _get_birthday(downloaded_files["profile"])
    return _process_matches(downloaded_files["career"], name, birthday)
