#MODULE 1
import os
import glob
import pandas as pd

#Store all game file names into a list, sorted. The game files all end in .EVE in the 'games' folder
gamefiles = glob.glob(os.path.join(os.getcwd), 'games', '*.EVE'))
game_files.sort()

#Read the game files into DataFrame
game_frames = []
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type','multi2','multi3','multi4','multi5','multi6','event'])
    game_frames.append(game_frame)

#Concatenate the DataFrames into one DataFrame called games
games = pd.concat(game_frames)

#Clean the data. Some rows have a value of '??' in the multi5 column 
games.loc[games['multi5'] == '??',['multi5']] = ''
