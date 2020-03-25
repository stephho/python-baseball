# MODULE 1
# GAME FILES: CLEAN AND IMPORT DATA

# Please refer to data.ipynb for more descriptive work

import os
import glob
import pandas as pd

# all of our game files live in the 'games' folder with extension .EVE. create a list of the file names of the game files
game_files = glob.glob(os.path.join(os.getcwd(), 'games','*.EVE'))
game_files.sort()

# read the game files into pandas dataframes
game_frames = []
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names = ['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

# concatenate the dataframes in game_frames into one dataframe
games = pd.concat(game_frames)

# clean 'multi5' column by replacing any rows that have a value of '??' with an empty starting
games.loc[games['multi5'] == '??', ['multi5']] = ''

# extract game id using regex into a dataframe called identifiers
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')

# not every row in games df has a game id, so the regex will return a n/a value in the identifiers df for those rows. we forward fill these n/a values with the preceding game id so that every row has a game id
identifiers = identifiers.fillna(method = 'ffill')

# rename column labels of identifiers dataframe
identifiers.columns = ['game_id', 'year']

# concatenate the identifiers df to the games df
games = pd.concat([games, identifiers], axis = 1, sort = False)

# replace the n/a values in the games df with empty strings
games = games.fillna('')

# this is the final, cleaned games dataframe!
games.head()
