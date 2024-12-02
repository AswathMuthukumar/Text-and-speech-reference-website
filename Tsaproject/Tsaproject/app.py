import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Set your Google API key as an environment variable
os.environ["GOOGLE_API_KEY"] = "AIzaSyDAB-iGvLbVycPoCYyrRSsq2L4NbfnrHqo"

# Configure the Gemini API
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

app = Flask(__name__)


def chatbot(prompt):
  """
  Interacts with the Gemini model to generate a response to the given prompt.
  """

  # Use GenerativeModel instead of Model
  model = genai.GenerativeModel("gemini-pro")  # Choose a suitable model
  # Pass the prompt as the first positional argument
  response = model.generate_content(prompt)  # Use generate_content method
  return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chatbot(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)




