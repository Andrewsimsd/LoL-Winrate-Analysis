# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 22:54:31 2020

@author: andre
"""

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os
import pickle
import pathlib

def main():
    save_file_dir = os.path.join(os.getcwd(), 'Artifacts')
    pathlib.Path(save_file_dir).mkdir(parents=True, exist_ok=True)
    # save_file_name = os.path.join(save_file_dir, 'results.txt')
    q = [r'https://na.op.gg/summoner/userName=John5un',
         r'https://na.op.gg/summoner/userName=o0OepicO0o',
         r'https://na.op.gg/summoner/userName=EG+Bae',
         r'https://na.op.gg/summoner/userName=go+in+idiot',
         r'https://na.op.gg/summoner/userName=DirtyMobs',
         r'https://na.op.gg/summoner/userName=H%C3%A3kurei+Reimu',
         r'https://na.op.gg/summoner/userName=SSJG+Vegito',
         r'https://na.op.gg/summoner/userName=Titan+Dweevil',
         r'https://na.op.gg/summoner/userName=Sunbee',
         r'https://na.op.gg/summoner/userName=Bodast',
         r'https://na.op.gg/summoner/userName=SSJG+Vegito',
         r'https://na.op.gg/summoner/userName=Titan+Dweevil',
      
        ]
    for url in q:
        # url = r'https://na.op.gg/summoner/userName=tfblade'
        pages = find_pages(url)
        for url in pages:
            try:
                calc_win_rates(url,save_file_dir)
            except:
                continue
    
    
def find_pages(base_page):
    name = base_page.split('Name=')[-1]
    uClient = uReq(base_page)
    page_html = uClient.read()
    uClient.close()
    #html parser
    page_soup = soup(page_html, 'html.parser')
    users = page_soup.findAll('div', {'class': 'SummonerName'})
    urls = []
   
    for user in users:
        if name not in user.a['href']:
            urls.append(r'https:' + user.a['href'])
    return urls


def calc_win_rates(url, save_file_dir):    
    name = url.split('Name=')[-1]
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    #html parser
    page_soup = soup(page_html, 'html.parser')
    users = page_soup.findAll('div', {'class': 'SummonerName'})
    try:
        win_ratio = int(str(page_soup.findAll('span', {'class': 'winratio'})[0]).split('%')[0].split(' ')[-1])
        rank = str(page_soup.findAll('div', {'class': 'TierRank'})[0]).split('<')[-2].split('>')[-1]
    except:
        return
    teams = []
    for i, user in enumerate(users):
        if name in str(user):
            if (i%10 < 5):
                teams.append(1)
            else:
                teams.append(2)
   
    enemy_win_ratios = []
    friendly_win_ratios = []
    
    for i, user in enumerate(users):
        user_url = r'https:' + user.a['href']
        user_uClient = uReq(user_url)
        user_page_html = user_uClient.read()
        user_uClient.close()
        user_page_soup = soup(user_page_html, 'html.parser')
        try:
            user_win_ratio = int(str(user_page_soup.findAll('span', {'class': 'winratio'})[0]).split('%')[0].split(' ')[-1])
        except:
            continue
        if name in user_url:
            continue
        if (i%10 < 5) & (teams[i//10] == 1):   
            friendly_win_ratios.append(user_win_ratio)
        elif (i%10 >= 5) & (teams[i//10] == 2):
            friendly_win_ratios.append(user_win_ratio)
        else:
                enemy_win_ratios.append(user_win_ratio)

    data = {
        'rank' : rank,
        'win_ratio' : win_ratio,
        'friendly_win_ratios' : friendly_win_ratios,
        'enemy_win_ratios' : enemy_win_ratios
        }
    save_file_name = os.path.join(save_file_dir, f'{name}.pickle')
    with open(save_file_name, 'wb') as fh:
        pickle.dump(data, fh) 
        
if __name__ == '__main__':
    main()