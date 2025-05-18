from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df = pd.read_csv("data/movies.csv")

# Preprocess movie metadata into a single text blob
df["metadata"] = df["title"] + " " + df["genres"] + " " + df["tags"] + " " + df["mood"]

# Vectorize metadata
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df["metadata"])

def recommend_movies(prefs):
    query_parts = []

    if prefs.get("genre"):
        query_parts.append(prefs["genre"])
    if prefs.get("sentiment"):
        query_parts.append(prefs["sentiment"])
    if prefs.get("year"):
        query_parts.append(str(prefs["year"]))

    query = " ".join(query_parts)
    query_vec = vectorizer.transform([query])

    # Compute cosine similarity
    cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = cosine_sim.argsort()[::-1][:5]

    if len(top_indices) == 0:
        return ["No matching movies found."]
    else:

        recommendations = []
        for idx in top_indices:
            title = df.iloc[idx]["title"]
            genres = df.iloc[idx]["genres"]
            recommendations.append({'title':f"{title}", 'genres': ", ".join(genres.split('|'))})
        return recommendations