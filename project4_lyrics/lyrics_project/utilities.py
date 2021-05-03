#!/usr/bin/env python
# coding: utf-8


import requests
from bs4 import BeautifulSoup
import re
import os
import csv
import pandas as pd
import glob
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#downloads
nltk.download('punkt')
nltk.download('stopwords')


# Web scraping functions

def format_artist_name (name):
    """
    format the artist's name as included in the lyrics' links
    the name is inputed as a string and the white spaces are used to split the name
    """

    name_parts = name.split()
    name_length = len(name_parts)
    author_name = []
    for x in range (0, name_length):
        author_name.append(name_parts[x])
    author_str =""
    result= "+".join(author_name, )

    return result

#
def get_lyric_urls(url, name):
    """
    extract the urls for the lyric pages from the artist's webpage
    """
    artist = format_artist_name(name)

    html_artist_page = requests.get(url).text
    parsed_html = BeautifulSoup(html_artist_page, features="lxml")
    links_in_html = parsed_html.find_all('a', href=True)

    lyric_url_list = []
    for link in links_in_html:
        try:
            if artist in link.get('href'):
               part_url = link.get('href')
               lyric_url_list.append("https://www.lyrics.com/track/" + part_url[7:])
        except:
            continue

    return lyric_url_list



def get_lyrics(url_list, name):
    """
    extract the lyrics and save them in txt files in a
    folder with the author name
    """

    artist = format_artist_name(name)
    current_wd = os.getcwd()
    new_d_name = artist.lower().replace("+", "_")
    artist_d = os.mkdir(current_wd+'/'+'lyrics'+'/'+new_d_name)

    metadata = [["song_num", "song_title"]]
    for url in url_list:
        r = requests.get(url)
        html_songpage = r.text
        parsed_html_songpage = BeautifulSoup(html_songpage, features="lxml")
        try:
            song_title = parsed_html_songpage.find_all("h1", attrs={'class': 'lyric-title'})[0].text
            song_text = parsed_html_songpage.find_all("pre")[0].text
            filename = re.search("\d+",url).group()
            metadata_song = [filename,song_title]
            metadata.append(metadata_song)
            path = current_wd +'/'+'lyrics'+'/'+new_d_name+'/'+ filename+".txt"

            with open(path, 'w') as file:
                file.write(song_text)
        except:
            continue

    path_metadata = os.path.join(current_wd, 'lyrics', new_d_name,  "metadata.csv")
    with open(path_metadata, 'w') as csv_file:
        csv_file_writer = csv.writer(csv_file)
        csv_file_writer.writerows(metadata)


# Functions for reading the parsed data

def read_metadata(name):
    """
    read the metadata file in a df and adds a column with the artist's name
    """
    artist = format_artist_name(name).lower().replace("+", "_")
    current_wd = os.getcwd()
    metadata_path_author =  os.path.join(current_wd, 'lyrics', artist, "metadata.csv")
    df_metadata = pd.read_csv(metadata_path_author)
    df_metadata['author']= name

    return df_metadata

def read_lyrics(name):
    """
    read the lyrics txt files and stores them in a df
    """
    artist = format_artist_name(name).lower().replace("+", "_")
    current_wd = os.getcwd()
    glob_path = os.path.join(current_wd,"lyrics", artist, '*.txt')
    txt_files = glob.glob(glob_path)


    lyrics_dict_artist ={ }
    for file in txt_files:
        filename = re.search(r"(\d+\d+\d+\d+)", file).group()
        txt_filename = filename + ".txt"
        with open (os.path.join(current_wd,"lyrics", artist, txt_filename), 'r+') as f:
            lyrics = f.read()
            lyrics_dict_artist.update({filename:lyrics})

    df_lyrics = pd.DataFrame.from_dict(lyrics_dict_artist, orient='index').reset_index()
    df_lyrics.columns =["song_num", "song_lyrics"]
    df_lyrics['song_num']= df_lyrics['song_num'].astype(np.int64)

    return df_lyrics


# Functions for cleaning the lyrics text_list

def clean_text_to_list(df):
    """
    clean the lyrics text and return the lyrics texts as a list of strings
    """

    df['cleaned_lyric'] = df['song_lyrics'].str.replace("\d+|\n|[.,:;!?]|\s", " ")
    text_list = df['cleaned_lyric'].tolist()
    nltk_stopwords = stopwords.words("english")
    my_stopwords = nltk_stopwords+['aa']
    tokens_list = [word_tokenize(text) for text in text_list]
    cleaned_tokens = []
    for text in tokens_list:
        cleaned_tokens_subl = []
        for token in text:
            if (token not in my_stopwords) and (len(token)>3):
                cleaned_tokens_subl.append(token)
        cleaned_tokens.append(cleaned_tokens_subl)
    cleaned_tokens_str_format = []
    for element in cleaned_tokens:
        my_str = " ".join(map(str, element))
        cleaned_tokens_str_format.append(my_str)
    df['cleaned_lyric'] = df['cleaned_lyric'].astype("string")
    list_cleaned_lyrics = df['cleaned_lyric'].tolist()

    return list_cleaned_lyrics
