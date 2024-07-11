import streamlit as st
import pickle
import pandas as pd
import requests
import base64
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bf0f651419d6953f83624f49b628a7ad'.format(movie_id))
    data=response.json()
    
    return "https://image.tmdb.org/t/p/w500/" +data['poster_path']
def recommend(movie):
    movie_ind=movies[movies['title']==movie].index[0]
    movie_list=sorted(list(enumerate(similarity[movie_ind])),reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

@st.cache
def load_model():
	  return pickle.load(open('Machine_Learning/Movie Recommendation System/movies.pkl','rb'))

movies_list= load_model()
@st.cache(hash_funcs={"MyUnhashableClass": lambda _: None}

#movies_list=pickle.load(open('Machine_Learning/Movie Recommendation System/movies.pkl','rb'))
movies=pd.DataFrame(movies_list)

def load_model1():
    return pickle.load(open('Machine_Learning/Movie Recommendation System/similarity.pkl','rb'))

similarity=load_model1()
@st.cache(hash_funcs={"MyUnhashableClass": lambda _: None}
      
#similarity=pickle.load(open('Machine_Learning/Movie Recommendation System/similarity.pkl','rb'))
st.title('Movie Recommendation System')
selected_moviename=st.selectbox('Select the Movie:',movies['title'].values)
if st.button('Recommend'):
    names,posters=recommend(selected_moviename)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.markdown(f"<h5>{names[0]}</h5>", unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        st.markdown(f"<h5>{names[1]}</h5>", unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        st.markdown(f"<h5>{names[2]}</h5>", unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        st.markdown(f"<h5>{names[3]}</h5>", unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        st.markdown(f"<h5>{names[4]}</h5>", unsafe_allow_html=True)
        st.image(posters[4])



    
