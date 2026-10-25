import streamlit as st


@st.cache_resource
def load_recommender():
    import vectorization

    return vectorization


st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title("Movie Recommender")
st.write("Choose a movie to discover similar titles.")

recommender = load_recommender()
movies = sorted(recommender.df["title"].dropna().unique().tolist())

selected_movie = st.selectbox("Select a movie", movies)

if st.button("Find recommendations", type="primary"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommender.suggest_movie(selected_movie)

    st.subheader(f"Movies similar to {selected_movie}")
    for index, movie in enumerate(recommendations, start=1):
        st.markdown(f"**{index}. {movie}**")
