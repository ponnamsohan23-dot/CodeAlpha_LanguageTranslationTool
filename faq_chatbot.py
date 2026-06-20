from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    "What is AI?",
    "What is Machine Learning?",
    "What is Python?",
    "What is Deep Learning?"
]

answers = [
    "AI is Artificial Intelligence.",
    "Machine Learning enables systems to learn from data.",
    "Python is a programming language.",
    "Deep Learning is a subset of Machine Learning."
]

vectorizer = TfidfVectorizer()

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    all_text = questions + [user_input]

    tfidf = vectorizer.fit_transform(all_text)

    similarity = cosine_similarity(
        tfidf[-1],
        tfidf[:-1]
    )

    index = similarity.argmax()

    print("Bot:", answers[index])