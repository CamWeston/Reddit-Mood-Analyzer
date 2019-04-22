import requests
import json
import re
from IPython.display import HTML


subscription_key = "71ce66c08c554bfda552d85b9eb168a8"
sentiment_api_url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"


def analyze(text):
        text = re.sub(r"[^a-zA-Z ,.!?'0-9]", " ", text)
        text = text[:5100]
        request_body ={
            "documents" : [{
                "id" : "1",
                "text": text
            }]
        }
        headers = {'Content-Type': 'application/json',"Ocp-Apim-Subscription-Key": subscription_key}
        response = requests.post(sentiment_api_url, headers=headers, json=request_body)
        response = response.text
        return response
