import json
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def load_faq_data():
    with open('chatbot/data/faq.json') as f:
        data = json.load(f)
    return data

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return tokens

def process_query(query, faq_data):
    query_tokens = preprocess_text(query)
    for faq in faq_data:
        if set(query_tokens).intersection(set(faq['keywords'])):
            return faq['answer']
    return "I'm sorry, I don't have the information you're looking for."

def get_response(user_input):
    faq_data = load_faq_data()
    response = process_query(user_input, faq_data)
    return response
