import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import requests
import pickle

#####################################
# Set Streamlit to full screen mode##
#####################################
st.set_page_config(
    page_title="Movies Recommender App",
    page_icon="🎬",
    layout="wide",  # You can adjust the layout as needed
    initial_sidebar_state="expanded",
)


########
# Intro#
########
selected = option_menu(
    menu_title=None,
    options=["Home", "App", "Contact"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "green"},
    },
)
##############
# Home Page##
##############
if selected == "Home":
    #st.write("<p style='color:blue; font-size: 30px; font-weight: bold;'>You have selected Home!🏡</p>", unsafe_allow_html=True)
    #st.title(f"You have selected {selected}")
    st.image("MoVies.png")

################
# Projects Page#
################
elif selected == "App":
    #st.title(f"You have selected {selected}")

    ### API to fetch movie posters
    def fetch_poster(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path

    ### Dataset fetch for "pkl" format
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    ### Helper function for movie recommendations
    def recommend(movie):
        index = movies[movies['title'] == movie].index[0] 
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]) 
        recommended_movie_names = []  
        recommended_movie_posters = []  
        for i in distances[1:6]:
            id = movies.iloc[i[0]].id
            recommended_movie_posters.append(fetch_poster(id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names, recommended_movie_posters

    movie_list = movies['title'].values 
    selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
###############
# Contact Page#
###############
elif selected == "Contact":
    #st.title(f"You have selected {selected}")

    
    
    ### About the author
    st.write("##### About the author:")
    
    ### Author name
    st.write("<p style='color:blue; font-size: 50px; font-weight: bold;'>Usama Munawar</p>", unsafe_allow_html=True)
    
    ### Connect on social media
    st.write("##### Connect with me on social media")
    
    ### Add social media links
    ### URLs for images
    linkedin_url = "https://img.icons8.com/color/48/000000/linkedin.png"
    github_url = "https://img.icons8.com/fluent/48/000000/github.png"
    youtube_url = "https://img.icons8.com/?size=50&id=19318&format=png"
    twitter_url = "https://img.icons8.com/color/48/000000/twitter.png"
    facebook_url = "https://img.icons8.com/color/48/000000/facebook-new.png"
    
    ### Redirect URLs
    linkedin_redirect_url = "https://www.linkedin.com/in/abu--usama"
    github_redirect_url = "https://github.com/UsamaMunawarr"
    youtube_redirect_url ="https://www.youtube.com/@CodeBaseStats"
    twitter_redirect_url = "https://twitter.com/Usama__Munawar?t=Wk-zJ88ybkEhYJpWMbMheg&s=09"
    facebook_redirect_url = "https://www.facebook.com/profile.php?id=100005320726463&mibextid=9R9pXO"
    
    ### Add links to images
    st.markdown(f'<a href="{github_redirect_url}"><img src="{github_url}" width="60" height="60"></a>'
                f'<a href="{linkedin_redirect_url}"><img src="{linkedin_url}" width="60" height="60"></a>'
                f'<a href="{youtube_redirect_url}"><img src="{youtube_url}" width="60" height="60"></a>'
                f'<a href="{twitter_redirect_url}"><img src="{twitter_url}" width="60" height="60"></a>'
                f'<a href="{facebook_redirect_url}"><img src="{facebook_url}" width="60" height="60"></a>', unsafe_allow_html=True)
##########################################
# Display a message if no page is selected#
##############################################
else:
    st.title("Welcome to the Movie Recommender App")
    st.write("Please select a page from the navigation menu on the left.")
####################
# Thank you message#
#####################
st.write("<p style='color:green; font-size: 30px; font-weight: bold;'>Thank you for using this app, share with your friends!😇</p>", unsafe_allow_html=True)
