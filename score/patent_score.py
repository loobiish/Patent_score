import joblib as joblib
import random

def score(title):
    patent_score = "patent_score.pkl"
    joblib_model = joblib.load(patent_score)

    score = joblib_model.predict([title])[0]
    return round(random.uniform(score-4, score+4), 2)