import requests
import json
from IPython.display import HTML


subscription_key = "71ce66c08c554bfda552d85b9eb168a8"
sentiment_api_url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"


def analyze(text):
        request_body = {
            "documents" : [{
                "id" : "1",
                "text": text
            }]
        }
        request_body = json.dumps(request_body)
        print(request_body)
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        response = requests.post(sentiment_api_url, headers=headers, json=request_body)
        return response.json()
