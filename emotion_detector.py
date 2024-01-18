import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=headers)

    formatted_response = response.json()
    emotions = formatted_response["emotionPredictions"][0]["emotion"];

    domEmotion = get_dominant_emotion(emotions);
    output = {
        "anger":emotions["anger"],
        "disgust":emotions["disgust"],
run        "fear":emotions["fear"],
        "joy":emotions["joy"],
        "sadness":emotions["sadness"],
        "dominant_emotion":domEmotion
    }
    return output;


def get_dominant_emotion(emotions):
    check = [
        "anger",
        "disgust",
        "fear",
        "joy",
        "sadness"
    ]

    dom = ""
    domVal = 0

    for name in check:
        if ( emotions[name] > domVal ):
            dom = name;
            domVal = emotions[name];
    return dom;




