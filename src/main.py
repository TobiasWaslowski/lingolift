import logging
import os

import openai
from dotenv import load_dotenv

from src.gpt.gpt_adapter import generate_translation, generate_breakdown, generate_responses
from src.util.mocks import mock_response

from flask import Flask, jsonify, request
from flask_cors import CORS

# setup
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

# configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/translate', methods=['POST'])
def get_translation():
    sentence = request.json.get('sentence')
    response = generate_translation(sentence)
    return jsonify(response)


@app.route('/responses', methods=['POST'])
def get_translation():
    sentence = request.json.get('sentence')
    response = generate_responses(sentence)
    return jsonify(response)


@app.route('/breakdown', methods=['POST'])
def get_translation():
    sentence = request.json.get('sentence')
    response = generate_breakdown(sentence)
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
