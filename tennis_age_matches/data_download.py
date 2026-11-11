import requests
from .process_data import process_matches, find_player, get_birthday

tennis_url = "https://www.tennisabstract.com"

def download_files(files):
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
    directory = download_files(player_dict)
    name, tour = find_player(player_name, directory["players"])
    player_id = "".join(letter for letter in name if letter.isalnum())
    player_profile = "wplayer.cgi" if tour == "(W)" else "player.cgi"
	
    files = {
        "career" : f"{tennis_url}/jsmatches/{player_id}Career.js",
        "profile" : f"{tennis_url}/cgi-bin/{player_profile}?p={player_id}"
	}

    downloaded_files = download_files(files)
    birthday = get_birthday(downloaded_files["profile"], name)
    return process_matches(downloaded_files["career", name, birthday])
    

# cwd = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.dirname(cwd)
# PATH_TO_DATA = os.path.join(project_root, "data")
# os.makedirs(PATH_TO_DATA, exist_ok=True) # ensure data directory exists

# files = { 
#     "SerenaWilliamsCareer.js" : "https://www.tennisabstract.com/jsmatches/SerenaWilliamsCareer.js",
# }

# for filename, url in files.items():
# 	get_request = requests.get(url)
# 	get_request.raise_for_status()
# 	with open(os.path.join(PATH_TO_DATA, filename), "wb") as file:
# 		file.write(get_request.content)

# # to run on command line at project root, do 
# #   `python scripts/data_download.py`