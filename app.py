import streamlit as st
import pickle
import requests



def fetch_poster(movie_id):
    # Replace 'YOUR_API_KEY' with your actual TMDb API key
    api_key = '679e2295e780f43d4aad7277a676eba9'
    
    # Construct the URL to fetch movie details using the movie_id
    url = f"https://api.themoviedb.org/3/movie/550?api_key={api_key}"
    
    # Fetch data from the API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            # Get the poster_path and construct the full URL for the poster image
            poster_path = data['poster_path']
            full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_path
        else:
            # Return a placeholder image URL if poster_path is not available
            return "https://via.placeholder.com/500x750"
    else:
        # Handle API request failure or invalid response
        return "Error: Unable to fetch poster image"
movies=pickle.load(open("movies_list.pkl",'rb'))
similarity=pickle.load(open("similarity.pkl",'rb'))
movies_list=movies['original_title'].values

st.header("Movie Recommendation System")

selected_movie=st.selectbox("Select a movie:",movies_list)

import streamlit.components.v1 as components
def recommend(movie):
    index=movies[movies["original_title"]==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].original_title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie,recommend_poster
if st.button("Recommend"):
    movie_name,movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 =st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
    
    

        