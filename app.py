import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_posters(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bb6840bed0e631d6091b59ae8a81f1db&language=en-US'.format(id))
    data = response.json()
    
    
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=bb6840bed0e631d6091b59ae8a81f1db&language=en-US'.format(id))
    
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def rec(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True,key = lambda x:x[1])[1:6]
    rec_movies = []
    rec_movies_posters = []
    
    for i in movies_list:
        id = movies.iloc[i[0]].id
        #Fetching posters from api: 
        rec_movies.append(movies.iloc[i[0]].title)
        #Fetching posters from apis:
        rec_movies_posters.append(fetch_posters(id))


    return rec_movies,rec_movies_posters

movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('MOVIES RECOMMEMDER SYSTEM')
selected_name = st.selectbox(
    'TYPE YOUR FAV MOVIE AND SEE OUR RECOMMENDATIONS',
    movies['title'].values)
    
if st.button('Recommend'):
    names,posters = rec(selected_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
    
