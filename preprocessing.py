import numpy as np
import pandas as pd
import ast

movies = pd.read_csv(r'6. RecommenderSystemProject\tmdb_5000_movies.csv')
credit = pd.read_csv(r'6. RecommenderSystemProject\tmdb_5000_credits.csv')

#merged both the tables into one
movies = movies.merge(credit,left_on='id',right_on='movie_id')

#dropping unwanted columns , because we need to create a movie recommender system and hence require only those columns which help us in creating this system
drop_col = ['budget','homepage','original_title','popularity','production_companies','production_countries','spoken_languages','runtime','movie_id','tagline','vote_average','vote_count','status','title_y','original_language','revenue','release_date']
movies = movies.drop(columns=drop_col)

#preprocessing data
movies.dropna(inplace=True)
movies.drop_duplicates(inplace=True)
movies['title'] = movies['title_x']
movies = movies.drop(columns=['title_x'])
movies = movies[['id','title','overview','genres','keywords','cast','crew']]


#CONVERTING THE GENRE,KEYWORD , CAST AND CREW COLUMNS FROM THEIR IMPOROPER STRING OF LIST OF DICTIONARY FORMAT TO LIST FORMAT 

# print(movies['genres'].iloc[0])
# print(movies['keywords'].iloc[0])
# print(movies['cast'].iloc[0])
# print(movies['crew'].iloc[0])

#GENRE , KEYWORD AND CAST
"""IN ALL 3 CASES WE NEED TO CONVERT THE STRING TO LIST OF DICTIONARY FIRST AND THEN EXTRACT ONLY THE VALUE IN THE NAME KEYWORD FOR EACH DICTIONARY SO THAT FOR EVERY ENTRY IN GENRE COLUMN CONSISTS OF ONYL THE LIST OF GENRES FOR THAT PARTICULAR MOVIE, SIMILARLY FOR KEYWORD AND CAST COLUMNS"""
"""using ast.literal_eval to convert string to list of dictionaries"""

def convert(obj) :
    lists = []
    for i in ast.literal_eval(obj) : 
        lists.append(i['name'])
    #return only top 15 cast
    return lists[:15]

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert)

#CREW column
"""For this column, we have to implement a similar function but here out of all the crew members we require the name of only the director so the function changes as such"""

def find_director(obj) :
    lists = []
    for i in ast.literal_eval(obj) : 
        if(i["job"] == "Director") :
            lists.append(i["name"])
    return lists
movies['crew'] = movies['crew'].apply(find_director)


#NOW CONVERTING THE OVERVIEW COLUMN INTO LIST
def string_to_list(obj) : 
    lists = []
    lists.append(obj)
    return lists
movies['overview'] = movies['overview'].apply(string_to_list)


#REMOVE SPACES FROM BETWEEN WORDS
movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])


#COLUMN TAG CREATION
"""Now after making appropriate changes in all the columns , we will now concatenate all those columns into a single new column called which contains all info about a particular movie and drop the other columns"""
movies['Tags'] = movies['overview']  + movies['genres']  + movies['keywords']  + movies['cast']  + movies['crew']
#join all list with space
movies['Tags'] = movies['Tags'].apply(lambda x:" ".join(x))
#convert everything to lower case
movies['Tags'] = movies['Tags'].apply(lambda x:x.lower())
movies = movies.drop(columns=['cast','crew','keywords','genres','overview'])


movies.to_csv(r'6. RecommenderSystemProject\cleaned_movies.csv',index=False)
# print(movies.info())
# print(movies.head())
