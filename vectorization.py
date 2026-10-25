"""In this file, we have vectorizaed the tag column, i.e in vectorization what we have done , is we have :
1. Combined all the tags of all the rows into a single string
2. Then picked the top k (k=5000) most occuring words in this string
3. Then for each row , we have created a vector which contains the number of times each word of the k words appeared in the tag of that row.
So in total we have a new 5000 * k matrix which will contain the number of times each of the 5000 words appeared in each row tag.

eg - 
    w1 w2 w3 w4 ..... w5000
r1   2  3  3  1        0
r2   0  0  0  1        3
r3   ...
.
.
.
r5000 ...

sklearn.feature_extraction.text.countvectorizer has been used to perfrom this whole process.

vectorization has been done so that given a particular movie we can identify movies similar to it and then recommend them to the user, since vectorization gives us vectors for each row, we can find rows similar to it based on the vectors


also STEMMING has been performed to convert every word to it's root word, using the nltk library
eg -> ['loving','loved','lovable','love'] all have same root word , i.e 'lov'
"""

from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
df = pd.read_csv(PROJECT_DIR / 'cleaned_movies.csv')

#STEMMING 
ps = PorterStemmer()
def stem(text) :
    y = []
    
    for i in text.split() : 
        y.append(ps.stem(i))
    
    return " ".join(y)
df['Tags'] = df['Tags'].apply(stem)


#VECTORIZATION
cv = CountVectorizer(
    max_features=5000,
    stop_words='english',#used to ignore words like the , a, is ,are , etc.
)

vectors = cv.fit_transform(df['Tags']).toarray()
#returns rows*5000 matrix
# print(vectors.shape)


#FIND COSINE SIMILARITY
"""What is cosine similarity and why is it needed ? 

So now, we have converted the tags into their root form and then found the top k most commonly used words and found how many times they occur in each row , i.e we vectorized the 
tags.
Now , what we need to do is to find how similar each vector is to each other , to do this we need to find the distance between the vectors ,but not the euclidean distance , the cosine distance , i.e degree wise how far vectors are from each other. 
If vectors same , then degree=0 , so cosine distance = cos(0) = 1.
If vectors are completly opposite , then degree=180 , so cosine distance = cos(180) = -1 and so on.

smaller the distance , more similar the movies

We do this by using the cosine similarity function of sklearn.metric"""

distance = cosine_similarity(vectors)
#gives cosine distance of each movie with every other movie



#NOW WE WRITE A FUNCTION WHICH WILL GIVE US THE LIST OF TOP 10 MOVIE RECOMMENDATIONS GIVEN THAT WE GIVE IT A MOVIE NAME
def suggest_movie(movie_narme) :
    #find movie index
    movie_index = df[df['title']==movie_narme].index[0]

    #find it's distance vector ,ie distance from other movies , from distance[]
    similarity_vector = distance[movie_index]

    #sort distances while keeping track of the indexes
    similarity_vector = list(enumerate(similarity_vector))
    similarity_vector = sorted(similarity_vector, key=lambda x: x[1], reverse=True)
    
    #find top 10 movies
    recommended_movie_indices = [x[0] for x in similarity_vector[1:11]]
    
    recommended_movies = []
    for i in recommended_movie_indices :
        recommended_movies.append(df.iloc[i,1])

    return recommended_movies
    
# print(suggest_movie('Spiderman'))
    