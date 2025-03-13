import requests

def emotion_detector(text_to_analyze):
    ''' This function will use Watson NLP library to 
    detect emotion in given text_to_analyze '''

    # Constants to make request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }

    # Making request
    response = requests.post(url, json = my_obj, headers = header)

    # Returning response text
    return response.text

