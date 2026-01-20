import json
from backend.sequence import predict_next

DATA_PATH = 'data/content.json'

def search_and_predict(query):
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
        result = search_topic(query)

    if not result:
        return None, None
    
    topic_name = result['topic'].split('-')[0].strip()
    predicted = predict_next(topic_name)

    return result, predicted
