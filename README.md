# Admission Chatbot

## Project Overview
This project is a chatbot designed to answer questions related to college admissions. It includes responses to queries about admission procedures, requirements, and deadlines.

## Features
- Admission-related Q&A
- User interaction with multiple questions in a single session
- Contextual understanding for personalized responses
- Optional backend integration for real-time information
- Error handling and user feedback

## Getting Started

### Prerequisites
- Python 3.6+
- Flask
- NLTK

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/AIML-Project-Series.git
    cd AIML-Project-Series
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000/`.

## Project Structure
- `app.py`: Main Flask application.
- `templates/index.html`: HTML template for the chatbot interface.
- `static/css/styles.css`: CSS for the chatbot interface.
- `static/js/chatbot.js`: JavaScript for handling user interactions.
- `chatbot/utils/nlp_utils.py`: Utility functions for natural language processing.
- `chatbot/data/faq.json`: JSON file containing FAQ data.
- `tests/test_chatbot.py`: Unit tests for the chatbot.

## Contributing
Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.
