import json
from watson_developer_cloud import ToneAnalyzerV3

API_KEY = "Insert your key here"
URL = "https://gateway.watsonplatform.net/tone-analyzer/api"

# IBM Watson connection. This method is called from home.py
def analyze_tone(text):
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey=API_KEY,
        url=URL
    )

    tone_analysis = tone_analyzer.tone({'text': text}, 'application/json', False).get_result()

    return json.dumps(tone_analysis, indent=2, sort_keys=True)
