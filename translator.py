## FAQ Chatbot

## Description

#The FAQ Chatbot is a simple AI-based application developed using Python. It is designed to answer frequently asked questions by matching user queries with predefined questions and providing the most relevant response.

#The chatbot uses Natural Language Processing (NLP) techniques and text similarity methods to understand user input and return accurate answers. This project demonstrates the basic working of an intelligent chatbot system.

## Features
#* Answers frequently asked questions automatically
#* Uses NLP for text processing
#* Matches user queries with stored FAQs
#* Provides quick and accurate responses
#* Simple and easy-to-use interface

# Technologies Used
#* Python
#* NLTK
#* Scikit-learn
#* TF-IDF Vectorizer
#* Cosine Similarity

## Conclusion
#This project demonstrates how Artificial Intelligence and Natural Language Processing can be used to build a basic chatbot. It helps users get instant answers to common questions and provides practical experience in chatbot development using Python.

from googletrans import Translator

translator = Translator()

print("===== Language Translation Tool =====")

text = input("Enter text: ")
src = input("Source language (en, hi, te, fr): ")
dest = input("Target language (en, hi, te, fr): ")

translated = translator.translate(text, src=src, dest=dest)

print("\nTranslated Text:")
print(translated.text)
