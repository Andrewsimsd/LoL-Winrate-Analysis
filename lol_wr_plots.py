# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:44:47 2020

@author: andre
"""

import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


def main():
    files_dir = os.path.join(os.getcwd(), 'Artifacts')
    files = [os.path.join( files_dir, f) for f in os.listdir(files_dir) if os.path.isfile(os.path.join(files_dir, f))]
    col_names = ['rank','win_ratio', 'friendly_win_ratios', 'enemy_win_ratios', 'rank_color', 'division']
    wr_df = pd.DataFrame(columns = col_names)
    for i, file in enumerate(files):
        with open(file, 'rb') as fh:
            data = pickle.load(fh)

        df = pd.DataFrame(
            {'rank' : data['rank'],
            'win_ratio' : data['win_ratio'],
            'friendly_win_ratios' : np.average(data['friendly_win_ratios']),
            'enemy_win_ratios' : np.average(data['enemy_win_ratios'])
             }, index = [i])
        wr_df = wr_df.append(df, ignore_index = True)
    #set colors & divisions
    for i, rank in enumerate(wr_df['rank']):
        if 'Iron' in rank:
            wr_df['rank_color'][i] = 'black'
            wr_df['division'][i] = 'Iron'
        elif 'Bronze' in rank:
            wr_df['rank_color'][i] = 'brown'
            wr_df['division'][i] = 'Bronze'
        elif 'Silver' in rank:
            wr_df['rank_color'][i] = 'grey'
            wr_df['division'][i] = 'Silver'
        elif 'Gold' in rank:
            wr_df['rank_color'][i] = 'yellow'
            wr_df['division'][i] = 'Gold'
        elif 'Platinum' in rank:
            wr_df['rank_color'][i] = 'green' 
            wr_df['division'][i] = 'Platinum'
        elif 'Diamond' in rank:
            wr_df['rank_color'][i] = 'blue'
            wr_df['division'][i] = 'Diamond'
        else: 
            wr_df['rank_color'][i] = 'red'
            wr_df['division'][i] = 'Master+'
            
            
    ranks = ['Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master+'] 
    rank_colors = ['black', 'brown', 'grey', 'yellow', 'green', 'blue', 'red']
    regr_lines = []
    figure = plt.figure()
    for i, rank in enumerate(ranks):
        regr = linear_model.LinearRegression()
        x_train = wr_df['win_ratio'][wr_df['division'] == rank].to_numpy().astype(int).reshape(-1, 1)
        y_train = wr_df['friendly_win_ratios'][wr_df['division'] == rank].to_numpy()
        regr.fit(x_train, y_train)
        wr_pred = regr.predict(wr_df['win_ratio'][wr_df['division'] == rank].to_numpy().astype(int).reshape(-1, 1))
        plt.title(f'Personal Win Ratio VS. Team Win Ratio\nAll')
        # plt.scatter(wr_df['win_ratio'][wr_df['division'] == rank], wr_df['friendly_win_ratios'][wr_df['division'] == rank], color = wr_df['rank_color'][wr_df['division'] == rank], edgecolors = 'black')
        plt.plot(wr_df['win_ratio'][wr_df['division'] == rank], wr_pred, color=rank_colors[i], linewidth=3)
        plt.xlabel('Player Win Ratio (%)')
        plt.ylabel('Friendly Team Win Ratio (%)')
        
        
    # ranks = ['Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master+'] 
    # regr_lines = []
    # for i, rank in enumerate(ranks):
    #     regr = linear_model.LinearRegression()
    #     x_train = wr_df['win_ratio'][wr_df['division'] == rank].to_numpy().astype(int).reshape(-1, 1)
    #     y_train = wr_df['friendly_win_ratios'][wr_df['division'] == rank].to_numpy()
    #     regr.fit(x_train, y_train)
    #     wr_pred = regr.predict(wr_df['win_ratio'][wr_df['division'] == rank].to_numpy().astype(int).reshape(-1, 1))
    #     figure = plt.figure()
    #     plt.title(f'Personal Win Ratio VS. Team Win Ratio\n{rank}')
    #     plt.scatter(wr_df['win_ratio'][wr_df['division'] == rank], wr_df['friendly_win_ratios'][wr_df['division'] == rank], color = wr_df['rank_color'][wr_df['division'] == rank], edgecolors = 'black')
    #     plt.plot(wr_df['win_ratio'][wr_df['division'] == rank], wr_pred, color='blue', linewidth=3)
    #     plt.xlabel('Player Win Ratio (%)')
    #     plt.ylabel('Friendly Team Win Ratio (%)')
        
    # ranks = ['Gold 4', 'Gold 3', 'Gold 2', 'Gold 1'] 
    # regr_lines = []
    # for rank in ranks:
    #     regr = linear_model.LinearRegression()
    #     x_train = wr_df['win_ratio'][wr_df['rank'] == rank].to_numpy().astype(int).reshape(-1, 1)
    #     y_train = wr_df['friendly_win_ratios'][wr_df['rank'] == rank].to_numpy()
    #     regr.fit(x_train, y_train)
    #     wr_pred = regr.predict(wr_df['win_ratio'][wr_df['rank'] == rank].to_numpy().astype(int).reshape(-1, 1))
    
    #     figure = plt.figure()
    #     plt.title(f'Personal Win Ratio VS. Team Win Ratio\n{rank}')
    #     plt.scatter(wr_df['win_ratio'][wr_df['rank'] == rank], wr_df['friendly_win_ratios'][wr_df['rank'] == rank], color = wr_df['rank_color'][wr_df['rank'] == rank], edgecolors = 'black')
    #     plt.plot(wr_df['win_ratio'][wr_df['rank'] == rank], wr_pred, color='blue', linewidth=3)
    #     plt.xlabel('Player Win Ratio (%)')
    #     plt.ylabel('Friendly Team Win Ratio (%)')    
    figure = plt.figure()
    plt.scatter(wr_df['friendly_win_ratios'], wr_df['enemy_win_ratios'])

    plt.xlabel('Friendly Team Win Ratio (%)')
    plt.ylabel('Enemy Team Win Ratio (%)')
if __name__ == '__main__':
    main()