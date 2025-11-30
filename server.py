"""
This module deploys the Emotion Detection application using the Flask framework.
It provides endpoints for the home page and emotion detection functionality.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("EmotionDetector")

@app.route("/")
def render_index_page():
    """Renders the index.html page for the home route."""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyzes the text provided in the query parameter using the emotion_detector function
    and returns a formatted string result or an error message.
    """
    # Retrieve the text to analyze from the URL query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function from the packaged module
    response = emotion_detector(text_to_analyze)

    # Check for error condition (dominant_emotion is None, indicating a status_code 400 error)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the required output string
    formatted_output = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_output

if __name__ == "__main__":
    # Deploy the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)