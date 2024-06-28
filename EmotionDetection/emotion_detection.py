import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    obj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = obj, headers=header, timeout=10)
    json_response = json.loads(response.text)
    
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    output = {'dominant_emotion': ''}
    max_val = 0
    for key, value in json_response['emotionPredictions'][0]['emotion'].items():
        output[key] = value
        if max_val < value:
            output['dominant_emotion'] = key
            max_val = value

    return output
    