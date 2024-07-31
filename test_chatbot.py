import unittest
from chatbot.utils.nlp_utils import get_response

class ChatbotTestCase(unittest.TestCase):
    def test_admission_requirements(self):
        response = get_response("What are the admission requirements?")
        self.assertIn("admission requirements", response)

    def test_application_deadline(self):
        response = get_response("What is the application deadline?")
        self.assertIn("application deadline", response)

    def test_unknown_query(self):
        response = get_response("How many students are enrolled?")
        self.assertIn("I'm sorry", response)

if __name__ == '__main__':
    unittest.main()
