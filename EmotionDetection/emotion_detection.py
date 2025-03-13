import requests
import json

def emotion_detector(text_to_analyze):
    ''' This function will use Watson NLP library to 
    detect emotion in given text_to_analyze '''

    # Constants to make request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }

    # Making request
    response = requests.post(url, json = my_obj, headers = header)

    # If response is 400 for empty values, return Nones
    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    
    formatted_response = json.loads(response.text)

    # Extracting emotions
    emotions = {
        "anger" : formatted_response["emotionPredictions"][0]["emotion"]["anger"],
        "disgust" : formatted_response["emotionPredictions"][0]["emotion"]["disgust"],
        "fear" : formatted_response["emotionPredictions"][0]["emotion"]["fear"],
        "joy" : formatted_response["emotionPredictions"][0]["emotion"]["joy"],
        "sadness" : formatted_response["emotionPredictions"][0]["emotion"]["sadness"] }
    emotions['dominant_emotion'] = max(emotions, key = emotions.get)

    # Returning response text
    return emotions

