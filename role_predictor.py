import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("datasets/resumes.csv")

# Vectorize resume text
vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(data["Resume_str"])

# Target column
y = data["Category"]

# Train model
model = LogisticRegression()

model.fit(X, y)

# Function to predict role
def predict_role(resume_text):

    vec = vectorizer.transform([resume_text])

    prediction = model.predict(vec)

    return prediction[0]