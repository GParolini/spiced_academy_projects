#!/usr/bin/env python
# coding: utf-8

# # Project 4: Web scraping and text classification


from colorama import init
from colorama import deinit
from colorama import Fore, Back, Style
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from utilities import *

#Color print in terminal
init()


# Scraping data for artist1
print(Style.BRIGHT + Fore.RED + "Welcome to your lyrics finder")
print(Fore.RED + "I can help you find the lyrics of your favourite artist on lyrics.com")
print(Fore.GREEN + "Please provide below the name of the artist")
name1=input()
print(Fore.GREEN + "Please provide below the link to the artist webpage on lyrics.com")
url1=input()

urls_lyrics_list1=get_lyric_urls(url1, name1)
lyrics_files1 = get_lyrics(urls_lyrics_list1, name1)

# Reading the scraped data for artist1
metadata_df1 = read_metadata(name1)
lyrics_df1 = read_lyrics(name1)
df_artist1 = metadata_df1.merge(lyrics_df1)



# Scraping data for artist2
print(Fore.RED + "You can select a second artist and then you can quiz me about the two artists")
print(Fore.GREEN + "Please provide below the name of the artist")
name2 =input()
print(Fore.GREEN + "Please provide below the link to the artist webpage on lyrics.com")
url2=input()

urls_lyrics_list2=get_lyric_urls(url2, name2)
lyrics_files2 = get_lyrics(urls_lyrics_list2, name2)

# Reading the scraped data for artist2
metadata_df2 = read_metadata(name2)
lyrics_df2 = read_lyrics(name2)
df_artist2 = metadata_df2.merge(lyrics_df2)


# Joining the two artists' dataframes
df = pd.concat([df_artist1, df_artist2])

#train-test split
X_train, X_test, y_train, y_test = train_test_split(df.drop(["author"], axis=1), df["author"],
                                                    test_size=0.2, random_state=42)

#cleaning the lyrics tests and transforming them in a list of strings
list_cleaned_lyrics_train = clean_text_to_list(X_train)
labels_train = y_train.tolist()

#Bag of words
vect = TfidfVectorizer()
X =  vect.fit_transform(list_cleaned_lyrics_train)

#Transforming the test set
list_cleaned_lyrics_test = clean_text_to_list(X_test)
X_test_transformed = vect.transform(list_cleaned_lyrics_test)

#Fitting a logistic regression model
model_lr = LogisticRegression(class_weight='balanced').fit(X, y_train)
score_lr = model_lr.score(X, y_train)

#Checking how the logistic regression model performs on the test set
ypred = model_lr.predict(X_test_transformed)
score_lr = model_lr.score(X_test_transformed,y_test)
probs_lr = model_lr.predict_proba(X_test_transformed)
print(Fore.RED + "I am a data savvy software.")
print(Fore.RED + "I can tell you that a logistic regression model applied to classify")
print(Fore.RED + "the data of your two artists has a score of ", Back.GREEN + str(score_lr))
print(Back.RESET + Fore.RED + "and the probabilities for each entry in the test set are as follow ", Fore.RESET + str(probs_lr))

#Fitting a Naive Bayes model
model_nb = MultinomialNB(alpha=1).fit(X, y_train)
model_nb.score(X, y_train)

#Checking how the Naive Bayes Model performs on the test set
ypred_nb = model_nb.predict(X_test_transformed)
score_nb = model_nb.score(X_test_transformed,y_test)
probs_nb = model_nb.predict_proba(X_test_transformed)
print(Back.RESET + Fore.RED + "Do no take me for a pedantic software, but I can also tell you that")
print(Fore.RED + "a Naive Bayes model applied to classify the data of your two artists has a score of ", Back.GREEN + str(score_nb))
print(Back.RESET + Fore.RED + "and the probabilities for each entry in the test set are as follow ", Back.RESET + Fore.RESET + str(probs_nb))


#Testing user input
print(Back.RESET + Fore.RED + "Now, please select a model between Logistic Regression and Naive Bayes.")
print(Fore.RED + "Then you can quiz me with a few of your favourite lyrics.")
print(Fore.RED + "I will tell you who is the author of the lyrics.")
print(Fore.GREEN + "Please input your model choice (LR for Logistic Regression and NB for Naive Bayes)")
model_to_use = input()
print(Fore.GREEN + "Please input some lyrics for me to examine: ")
user_lyrics = input()

user_lyrics_transformed = vect.transform([user_lyrics])

if model_to_use=="LR":
    lr_pred = model_lr.predict(user_lyrics_transformed)
    lr_prob = model_lr.predict_proba(user_lyrics_transformed)
    print(Fore.YELLOW + Back.BLACK + str(lr_pred), str(lr_prob))
if model_to_use=="NB":
    nb_pred = model_nb.predict(user_lyrics_transformed)
    nb_prob = model_nb.predict_proba(user_lyrics_transformed)
    print(Fore.YELLOW + Back.BLACK + str(nb_pred), str(nb_prob))
if (model_to_use !="LR") and (model_to_use !="NB"):
    out = "You did not select a valid model"
    print(Fore.YELLOW + Back.BLACK + out)

deinit()
