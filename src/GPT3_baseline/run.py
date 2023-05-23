# app.py
from flask import Flask, render_template, request
import openai

openai.api_key = "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"

messages=[
    {"role": "system", "content": "You are a helpful and friendly language model. Your job is to analyze user input and recommend music based on their input. If a message is not music related, find a way to relate it to a song and recommend that song to the user."}
]

model = "gpt-3.5-turbo"

app = Flask(__name__)

# Set up OpenAI GPT API credentials
openai.api_key = "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"

# Define your GPT prompt
prompt = "You should listen to"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['input_string']

    # Concatenate user input with the GPT prompt
    input_text = f"{prompt}: {user_input}"
    messages.append({"role": "user", "content": input_text})
    # Generate music recommendation using OpenAI GPT
    # response = openai.Completion.create(
    #     engine='text-davinci-003',
    #     prompt=input_text,
    #     max_tokens=50,  # Adjust the max_tokens value to control the response length
    #     temperature=0.7,  # Adjust the temperature value to control the randomness of the response
    #     n=1  # Number of responses to generate
    # )
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    bot_response = response.choices[0]["message"]["content"]
    messages.append({"role": "assistant", "content": bot_response})

    return render_template('index.html', recommendation=bot_response)

if __name__ == '__main__':
    app.run(debug=True)
