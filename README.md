# Homework 3 - R/Python Package

**Author**: Melanie T. Huynh

## Description
This repository is an extension of HW 1 and HW 2 of Stat159/259 Fall 2026. The assignment involves creating a Python package for retrieving the career matches of a given player from tennisabstract.com, and plotting the New York Times (NYT) data visualization completed in HW 2 for any player in the [Tennis Abstract](http://www.tennisabstract.com) directory who has career match data. 

### Source Data
This package retrieves player profile and career match data from [Tennis Abstract](http://www.tennisabstract.com). Career files record opponent age differently, where we find some provide the player's birth date while others provide the player's age at the match date. Testing scripts use pre-saved JS files for two players, containing three matches of each format for testing, saved in the `data/` folder. 

## Installation Instructions
This package uses Python 3.10 or later versions. 

Run the following command in terminal to install the package along with its dependencies:
```
python -m pip install git+https://github.com/UCB-stat159-f26/hw03-2-huynmela.git
```

## How To Use 

### Main Functions
Below are instructions and descriptions of the two main functions of this package:

`get_player_matches(player_name)::DataFrame` is a pandas DataFrame where rows are matches containing six columns: `Match Date`, `Player`, `Opponent`, `Player Age`, `Opponent Age`, and `Player Won`. The function takes as input any variations of the player name e.g. `"serena williams"`, `"Serena Williams"`, or `"SerenaWilliams"`. If a name that is not in the Tennis Abstract directory is supplied e.g. `"GastonSanchez"`, the function will raise a `ValueError` indicating that the player could not be found. 

`plot_player_matches(player)` is a plotting function that takes a player's DataFrame containing their career profile and returns a Matplotlib figure. The x-axis is the player's age at the time of the match, while the y-axis is the player's and their opponent's age difference in years. Each point in the figure represents a match. Points above the x-axis indicate that the player is older than their opponent. Blue points represent player wins, while purple points represent player losses. 

You can view the plots by running something like:
```python
import matplotlib.pyplot as plt
from tennis_age_matches import get_player_matches, plot_player_matches

serena = get_player_matches("serena williams")
print(serena.head())
plot_player_matches(serena)
plt.show()
```

### Test Functions
To run the tests, at the root of this repository, you must have the package `pytest` installed. Run the following on the command line:
```
python -m pip install -e .pytest
python -m pytest -v tennis_age_matches/tests/test_process_data.py
```
This will run four tests, but they do not download the data from online. Instead, they use offline saved data, located in `data/`. This is meant to check the match dates, opponent names, ages, and match results. Additionally, two test the different spellings of the player names and checks the error raised when supplying a name that is not in Tennis Abstract. 

## File Structure

```{.markdown code-line-numbers="false"}
hw03-2-huynmela/
    README.md
    instructions.md
    pyproject.toml
    data/ 
        FemalePlayerCareer.js
        MalePlayerCareer.js
    tennis_age_matches/
        __init__.py
        data_download.py
        process_data.py
        make_plot.py
        tests/
            test_process_data.py
```

## Personal Reflection
In this assignment, I found it difficult to write consistent commit messages when I had to carry the same change through multiple files. In the past, I usually would use `git add .`, but this time I tried to commit one file at a time every time I made a change so that each file had its own message, and I pushed after each commit. This became a tad tedious, especially when all I had done was change the naming convention for a variable. I would update the name in the script where I defined it, update it again in the script where I used it, and then find myself trying to write two unique messages for what was really one change. Looking back, I could have committed those files together and written one message that explained the rename, but that would defeat the purpose of being intentionally tedious in regular, detailed commits. 

Even so, going through the files one at a time helped me remember which functions I had written in each script and where I was calling them. I felt far more organized than I had in HW 2. When I sat down to write the `README.md`, I could follow how a player’s name became a data frame and how that same data frame was used to make the plot. This was a fulfilling assignment for me, and I hope to carry this practice into every project I work on from now on. I think coupling modularity with documentation will be especially useful when I write larger packages. Taking the time to explain how the pieces fit together helps me know my own work deeply enough that I can come back to it later without getting lost in my own code.
