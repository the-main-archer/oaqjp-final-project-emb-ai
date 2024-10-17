import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion_predictions.get('anger', 0)
        disgust_score = emotion_predictions.get('disgust', 0)
        fear_score = emotion_predictions.get('fear', 0)
        joy_score = emotion_predictions.get('joy', 0)
        sadness_score = emotion_predictions.get('sadness', 0)
        dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion[0]
        }
    
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
