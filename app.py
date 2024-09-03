from flask import Flask, request, jsonify
import d20
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the root route
@app.route http://127.0.0.1:5000/
def home():
    return "Welcome to the D&D Dice Roller!"

# Define the roll route
@app.route http://127.0.0.1:5000/roll methods=['POST']
def roll_dice_api():
    data = request.get_json()
    expression = data.get('expression')

    roll_result = roll_dice(expression)
    gpt_response = chat_with_gpt(f"The player rolled {expression} with the result: {roll_result}. Provide some narrative.")

    return jsonify({
        "roll_result": roll_result,
        "gpt_response": gpt_response
    })

def roll_dice(expression):
    try:
        result = d20.roll(expression)
        return f"Roll: {result}\nTotal: {result.total}\nDetailed Rolls: {result.result}"
    except d20.errors.RollSyntaxError as e:
        return f"Syntax Error: {e}"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Use "gpt-4" if you have access
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
