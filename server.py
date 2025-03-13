''' This is for the final project
    This creates web deployment for emotion detection
'''

# imports
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Create app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotionDetector():
    ''' This executes emotion_detector '''
    # Retrieve text to analyze
    text_to_analyze = request.args.get('textToAnalyze')

    # Analyze text
    response = emotion_detector(text_to_analyze)

    # Extract values
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    # Return
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear},' joy': {joy}, 'sadness': {sadness}. The dominant emotion is {dominant}"

@app.route("/")
def render_index():
    ''' function displays index '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This function executes the flask app on localhost:5000 '''
    app.run(host = "0.0.0.0", port = 5000)