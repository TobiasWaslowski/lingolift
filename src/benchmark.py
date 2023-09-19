import logging
import os
import unittest

import openai
from dacite import from_dict
from dacite.exceptions import DaciteError
from dotenv import load_dotenv

from src.domain.response_suggestion import ResponseSuggestion
from src.domain.sentence_component import SentenceComponent
from src.domain.translation import Translation
from src.gpt.gpt_adapter import _openai_exchange, _parse_response, generate_translation, generate_responses, \
    generate_syntactical_analysis
from src.gpt.message import SYSTEM, Message, USER
from src.gpt.prompts import SYSTEM_PROMPT


class Benchmark(unittest.TestCase):
    BENCHMARK_SENTENCES = [
        "Как у тебя сегодня дела?",
        "Hvordan har du det i dag?",
        "Apa kabarmu hari ini?",
        "Como você está hoje?"
    ]

    def setUp(self) -> None:
        load_dotenv()
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    def test_benchmark_summary(self):
        error_count = 0
        for sentence in self.BENCHMARK_SENTENCES:
            logging.info(f"Getting response suggestions for {sentence} ...")
            try:
                openai_response = generate_responses(sentence)
                response_suggestions = openai_response['response_suggestions']
                for suggestion in response_suggestions:
                    from_dict(data_class=ResponseSuggestion, data=suggestion)
            except ValueError as ve:
                logging.error(f"Could not parse JSON: {ve}")
                error_count = error_count + 1
                continue
            except DaciteError as de:
                logging.error(f"Error serializing JSON to dataclass: {de}")
                error_count = error_count + 1
        self.assertLessEqual(error_count, 1)

    def test_benchmark_responses(self):
        error_count = 0
        for sentence in self.BENCHMARK_SENTENCES:
            logging.info(f"Getting translation for {sentence} ...")
            try:
                response = generate_responses(sentence)
                from_dict(data_class=ResponseSuggestion, data=response)
            except ValueError as ve:
                logging.error(f"Could not parse JSON: {ve}")
                error_count = error_count + 1
                continue
            except DaciteError as de:
                logging.error(f"Error serializing JSON to dataclass: {de}")
                error_count = error_count + 1
        self.assertLessEqual(error_count, 1)

    def test_benchmark_grammatical_analysis(self):
        error_count = 0
        for sentence in self.BENCHMARK_SENTENCES:
            logging.info(f"Getting syntactical analysis for {sentence} ...")
            try:
                response = generate_syntactical_analysis(sentence)
                analysis = response['syntactical_analysis']
                for component in analysis:
                    from_dict(data_class=SentenceComponent, data=component)
            except (ValueError, KeyError):
                logging.error(f"Could not parse JSON: {response}")
                error_count = error_count + 1
                continue
            except DaciteError as de:
                logging.error(f"Error serializing JSON to dataclass: {de}")
                error_count = error_count + 1
        self.assertLessEqual(error_count, 1)


if __name__ == "__main__":
    unittest.main()
