import re

def extract_genre(text):
    genres = ["comedy", "drama", "romance", "thriller", "action", "adventure", "crime", "biography", "mystery", "music"]
    for genre in genres:
        if genre.lower() in text.lower():
            return genre.lower()
    return None

def extract_sentiment(text):
    if any(word in text.lower() for word in ["happy", "light", "fun", "uplifting", "love", "great", "good"]):
        return "positive"
    elif any(word in text.lower() for word in ["sad", "serious", "dark", "intense", "tragic"]):
        return "negative"
    else:
        return "neutral"

def extract_year(text):
    match = re.search(r"(\b19\d{2}\b|\b20\d{2}\b)", text)
    return int(match.group()) if match else None

def extract_preferences(text):
    return {
        "genre": extract_genre(text),
        "sentiment": extract_sentiment(text),
        "year": extract_year(text)
    }
