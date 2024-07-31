from flask import Flask, render_template, request, jsonify
import os
import nltk
from chatbot.utils.nlp_utils import process_query, get_response

app = Flask(__name__)

# Ensure NLTK data is downloaded
nltk.download('punkt')
nltk.download('wordnet')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
