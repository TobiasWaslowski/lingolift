from src.gpt.message import Message, SYSTEM
from src.gpt.prompts import *

EMPTY_CONTEXT = [Message(role=SYSTEM, content=SYSTEM_PROMPT)]
TRANSLATION_CONTEXT = [Message(role=SYSTEM, content=TRANSLATION_SYSTEM_PROMPT)]
RESPONSES_CONTEXT = [Message(role=SYSTEM, content=RESPONSES_SYSTEM_PROMPT)]
SYNTACTICAL_ANALYSIS_CONTEXT = [Message(role=SYSTEM, content=SYNTACTICAL_ANALYSIS_SYSTEM_PROMPT)]