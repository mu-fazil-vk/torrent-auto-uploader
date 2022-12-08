"""
===========================Fazil vk============================

©️ Copyrighted by Fazil vk: https:github.com/mu-fazil-vk
⚠️ Do not remove this caption

===============================================================
"""

import os
import requests
from bs4 import BeautifulSoup
import time
from tele import bot
from os.path import exists

Title = ''

while True:
    title = ''
    Link = ''
    Dl_f_link = ''
    Dl_link = ''
    url = 'https://dvdplex.com/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    movie = soup.find_all("p", {"class": "home"})
    # print(movie)
    for movies in movie:
        title_element = movies.find("a")
        title = title_element["title"]
        link_element = title_element["href"]
        link = "https://dvdplex.com/" + link_element
        title = title
        Link = link
        break
    if Title == title:
        time.sleep(300)
        continue
    else:
        Title = title
        print(Title)
        res = requests.get(Link)
        soup = BeautifulSoup(res.text, 'lxml')
        movie = soup.find("a", {"class": "touch"})
        co_link = "https://dvdplex.com/" + movie["href"]
        la_link = co_link

        res = requests.get(la_link)
        soup = BeautifulSoup(res.text, 'lxml')
        movie_dl = soup.findAll("a", {"class": "touch"})
        for movies_dl in movie_dl:
            dl_f_link = movies_dl['href']
            dl_s_link = "https://dvdplex.com//" + dl_f_link
            Dl_f_link = dl_s_link
            break

        res = requests.get(Dl_f_link)
        soup = BeautifulSoup(res.text, 'lxml')
        movie_dl = soup.findAll("a")

        for movies_dl in movie_dl:
            if movies_dl.text == "Download File(Direct Link)":
                dl = "https://dvdplex.com//" + movies_dl["href"]
                Dl_link = dl
                break
        if Dl_link == '':
            for movies_dl in movie_dl:
                if movies_dl.text == "Download File(UploadBox Server )":
                    dl = movies_dl["href"]
                    Dl_link = dl
                    print(dl)
                    break
        dl_file_link = Dl_link

        local_filename_tmp = Link.split('/')[-1] + '.mkv'
        local_filename = local_filename_tmp.replace(' ', '_').replace(':', '_')
        file_path = os.path.join('temp', local_filename)

        print('Download started ' + local_filename)
        # NOTE the stream=True parameter below
        with requests.get(dl_file_link, stream=True) as r:
            r.raise_for_status()
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    # if chunk:
                    f.write(chunk)

        time.sleep(200)
        file_exists = exists(file_path)
        if file_exists:
            bot.send(file_path)
        elif not file_exists:
            time.sleep(500)
            file_exists_final = exists(file_path)
            if file_exists_final:
                bot.send(file_path)
                time.sleep(300)
                os.remove(file_path)
