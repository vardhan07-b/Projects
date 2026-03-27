import streamlit as st
import joblib

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# ----------------------------
# Custom Color Theme
# ----------------------------
st.markdown("""
<style>

/* Main background gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #F72585, #7209B7, #4CC9F0);
    color: white;
}

/* Remove white header */
[data-testid="stHeader"] {
    background: transparent;
}

/* Center container styling */
.main .block-container {
    background: rgba(255, 255, 255, 0.1);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

/* Title */
h1 {
    text-align: center;
    font-size: 42px;
    color: #ffffff;
    font-weight: bold;
}

/* Subtitle */
h3 {
    text-align: center;
    color: #e0e0ff;
}

/* Selectbox label */
.stSelectbox label {
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
}

/* Dropdown styling */
div[data-baseweb="select"] {
    background-color: rgba(255, 255, 255, 0.2) !important;
    color: white !important;
    border-radius: 12px;
}

/* Button Styling */
.stButton>button {
    background: linear-gradient(45deg, #00F5D4, #B5179E);
    color: white;
    border-radius: 30px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(45deg, #B5179E, #00F5D4);
}

/* Success box */
.stSuccess {
    background-color: rgba(255,255,255,0.2) !important;
    color: white !important;
    border-radius: 15px;
}

/* Hide footer */
footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Load Model
# ----------------------------
movies = joblib.load("movies.pkl")
cosine_sim = joblib.load("cosine_similarity.pkl")

indices = {title: i for i, title in enumerate(movies['title'])}

# ----------------------------
# Recommendation Function
# ----------------------------
def recommend_movies(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

# ----------------------------
# UI Layout
# ----------------------------
st.title("🎬 Movie Recommendation System")
st.markdown("### Find movies similar to your favorites 🍿")

selected_movie = st.selectbox(
    "🎥 Choose a movie",
    movies['title']
)

if st.button("✨ Get Recommendations"):
    st.success("Here are your top 5 picks:")
    recommendations = recommend_movies(selected_movie)
    
    for i, movie in enumerate(recommendations, 1):
        st.markdown(f"🌟 **{i}. {movie}**")

st.markdown("---")
