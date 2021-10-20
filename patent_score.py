import joblib as joblib
import random

patent_score = "patent_score.pkl"
joblib_model = joblib.load(patent_score)


score = joblib_model.predict([input()])[0]

print(round(random.uniform(score-4, score+4), 2))