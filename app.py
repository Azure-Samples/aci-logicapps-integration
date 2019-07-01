import os
from pprint import pprint
import requests
text_analytics_base_url = os.environ["BASE_URL"]
subscription_key = os.environ["SUBSCRIPTION_KEY"]
sentiment_api_url = text_analytics_base_url + "sentiment"
documents = {'documents': [
    {'id': '1', 'language': 'en',
        'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'}
]}
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)
