"""Server module for EmotionDetector."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detector import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Function which parses the emotion detected into a string for html."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."
    return ("The given statement, the system response is 'anger': " + str(response["anger"]) +
        ", 'disgust': " + str(response["disgust"]) +
        ", 'fear': " + str(response["fear"]) +
        ", 'joy': " + str(response["joy"]) +
        ", 'sadness': " + str(response["sadness"]) +
        ". The dominant emotion is" + response["dominant_emotion"])

@app.route("/")
def render_index_page():
    """Function which returns the index html template."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
