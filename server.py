''' Executing this function initiates the application of Emotion
    Detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, url_for, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def get_emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows a dictionary with each
        emotion and it's score.
    '''
    text = request.args.get("textToAnalyze")
    output = emotion_detector(text)
    if output['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    
    response = f"""For the given statement, the system response is 'anger': {output['anger']},
                'disgust': {output['disgust']},'fear': {output['fear']}, 'joy': {output['joy']}
                and 'sadness': {output['sadness']}. The dominant emotion is {output['dominant_emotion']}."""    
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
