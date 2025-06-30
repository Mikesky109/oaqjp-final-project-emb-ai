''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned emotion rate and its dominant emotion for the provided text.
    '''
    text_to_detect = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_detect)

    emotion_rate_list = list(response.items())[:-1]
    emotion_rate_string = ', '.join(f'"{key}": {value}' for key, value in emotion_rate_list)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is {emotion_rate_string}. "
            f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
