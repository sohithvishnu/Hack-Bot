import openai
import os
from dotenv import load_dotenv
load_dotenv()

def predict_pipeline(question):
    openai.api_key = os.getenv("api-key")
    fine_tuned_model = "davinci:ft-personal-2023-05-18-21-33-55"
    answer = openai.Completion.create(
        model=fine_tuned_model,
        prompt=question
    )
    return str(answer['choices'][0]['text'])