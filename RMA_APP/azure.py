import requests
import json
import re
from IPython.display import HTML


subscription_key = "Insert your key here"
sentiment_api_url = "Insert your key here"


def analyze(text):
        text = re.sub(r"[^a-zA-Z ,.!?'0-9]", " ", text)
        text_length = len(text)
        text_segments = round(text_length/5100)-1
        headers = {'Content-Type': 'application/json',"Ocp-Apim-Subscription-Key": subscription_key}
        texts = []
        scores = []
        i = 0
        for i in range(0,text_segments-1):
                temp_text = text
                texts.append(temp_text[5100*i:5100*(i+1)])
                request_body ={
                    "documents" : [{
                        "id" : "1",
                        "text": texts[i]
                    }]
                } 
                response = requests.post(sentiment_api_url, headers=headers, json=request_body)
                response = response.text
                response = json.loads(response)
                for tone in response['documents']:
                        scores.append({
                                'score_id':tone['id'],
                                'score':tone['score']
                        })
        total = 0
        for score in scores:
                score_num = float(score['score'])
                total += score_num
        avg_score = total/text_segments
        azure_score = []
        azure_score.append({
                'score_id':1,
                'score':avg_score
        })
        return azure_score
