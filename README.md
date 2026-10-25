# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python and Machine Learning. The project analyzes movie metadata to recommend movies similar to a user's selected movie.

The system recommends movies similar to a user's selected movie by analyzing movie metadata, transforming textual features into numerical vectors, and calculating similarity scores between movies.

The project demonstrates data preprocessing, feature engineering, text vectorization, similarity-based ranking, and the development of a machine learning application.


## 📖 Project Overview

Movie recommendation platforms help users discover movies based on their interests and viewing preferences.

This project implements a content-based filtering recommendation system that identifies movies with similar characteristics based on their metadata.

Instead of predicting movie ratings or training a conventional supervised classification model, the system represents movies as numerical vectors and calculates their similarity.

When a user selects a movie, the system ranks other movies according to their similarity scores and returns the most relevant recommendations.

The application combines a Python-based recommendation engine with a Streamlit interface, allowing users to interact with the system through a web browser.



## 🚀 Features

- **Content-Based Filtering:** Recommends movies based on similarities in their metadata.
- **Text Vectorization:** Converts movie tags into numerical representations for similarity calculations.
- **Similarity-Based Ranking:** Ranks movies based on their similarity scores.
- **Interactive Interface:** Uses Streamlit to provide a simple interface for entering movie titles and viewing recommendations.
- **Data Preprocessing:** Cleans and combines movie metadata to prepare the dataset for recommendation.

## 🛠️ Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Frontend:** Streamlit
- **Dataset:** TMDB 5000 Movies Dataset

## 📂 Project Structure

```text
RecommenderSystemProject/
├── app.py                  # Streamlit frontend
├── vectorization.py        # Vectorization and recommendation logic
├── preprocessing.py        # Data preprocessing
├── cleaned_movies.csv      # Processed movie dataset
├── requirements.txt        # Python dependencies
├── tmdb_5000_movies.csv    # Original movie metadata (optional)
└── tmdb_5000_credits.csv   # Original cast and crew data (optional)
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd RecommenderSystemProject
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 How It Works

1. **Data Preprocessing:** Movie metadata is cleaned and transformed into a format suitable for analysis.
2. **Feature Engineering:** Relevant movie attributes are combined into textual tags representing each movie.
3. **Vectorization:** Textual tags are converted into numerical vectors using a text vectorization technique.
4. **Similarity Calculation:** Similarity scores are calculated between movies using the resulting vectors.
5. **Recommendation Generation:** Movies are ranked by similarity, and the most similar movies are returned as recommendations.

## 📊 Dataset

This project uses the TMDB 5000 Movies Dataset, which includes movie information and associated credits.

The original dataset files can be obtained from Kaggle. Ensure that the dataset's applicable terms are followed when using or redistributing the files.

## 🔮 Future Improvements

- Display movie posters and additional movie information.
- Add fuzzy matching to handle misspelled movie titles.
- Improve the interface with movie search and filtering.
- Deploy the application so users can access it online.

## 👨‍💻 Author

**Kavish Desai**

---

*Built as a hands-on project to explore content-based recommendation systems, text vectorization, and similarity-based ranking.*