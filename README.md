

#  NLP based Movie Recommender App

A hands-on NLP based movie recommendation system that understands natural language conversations and suggests movies based on **genre**, **sentiment**, **year**, and **user preferences**.

---

##  Features

-  **RegXX** for natural language understanding
-  Extracts user preferences (genre, year, sentiment) via LLM or local NLP
-  Movie recommendations using **Cosine Similarity** vector similarity
-  Frontend built with **Streamlit**
-  Easily extensible with custom datasets and models

---


##  Installation

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```


---

##  Sample Flow

1. Start the app:

i. Backend
```bash
uvicorn main:app --reload
```

ii. Frontend
```bash
streamlit run app.py
```

2. Enter a query like:

```
Suggest me an emotional Bollywood drama from the early 2000s
```

3. The system:
   - Extracts preferences from your message
   - Uses vector similarity to match movies
   - Displays the top 3 recommended titles

---

##  Recommendation Logic

- Uses **google/flan-t5-base** a open source free model for instruction-based parsing

- Uses **FAISS** to vectorize and match:
  ```
  metadata = title + genres + tags + mood
  ```


---

##  Data Format – `movies.csv`

| title            | genres  | year | tags     | mood      | sentiment |
|------------------|---------|------|----------|-----------|-----------|
| 3 Idiots         | Comedy  | 2009 | college  | uplifting | 0.72      |
| Dangal           | Drama   | 2016 | wrestling| inspiring | 0.88      |
| Andaz Apna Apna  | Comedy  | 1994 | classic  | funny     | 0.60      |

---


##  Acknowledgements

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [FastAPI] (https://fastapi.tiangolo.com)
