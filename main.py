from fastapi import FastAPI
from pydantic import BaseModel
from app.recommender import recommend_movies
from app.nlp_parser import extract_preferences

app = FastAPI()

class UserInput(BaseModel):
    message: str

@app.post("/recommend")
def recommend(user_input: UserInput):
    prefs = extract_preferences(user_input.message)
 
    recommendations = recommend_movies(prefs)
    if not 'No matching movies found' in recommendations:
        return {"result": True,"recommended_movies": recommendations}
    else:
        return {"recommended_movies": recommendations}