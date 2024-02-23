import streamlit as st
import pickle
import pandas as pd
import requests

def ftech(movie_id):
    requests.get
def recommend(movie):
    df_index=movies[movies['title']==movie].index[0]
    dis=sim[df_index]
    movie_list= sorted(list(enumerate(dis)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies          
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

sim=pickle.load(open('sim.pkl','rb'))
st.title('Movie Recommender System')
selected_movies_name=st.selectbox(
    'Which movie do you like to see?',
    movies['title'].values
)
if st.button('Recommend'):
    recommendation =recommend(selected_movies_name)
    for i in recommendation:
        st.write(i)