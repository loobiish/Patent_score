from sklearn.feature_extraction.text import CountVectorizer
import joblib as joblib
import random
import numpy as np

vec = CountVectorizer(stop_words='english')
joblib_file = "joblib_model.pkl"
joblib_model = joblib.load(joblib_file)

x = ['OpenCV Project', 'Smart Cleaning Tool', 'Green India', 'Hard Chipset',
 'Computer Network and System', 'Doorknobs', 'Smart Energy Meter']

x = vec.fit_transform(x).toarray()
score = joblib_model.predict(vec.transform([input()]))[0]

print(round(random.uniform(score-4, score+4), 2))