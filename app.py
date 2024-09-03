import requests

# Function to roll dice by sending a request to the Flask API
def roll_dice(expression):
    url = "http://127.0.0.1:5000/roll"
    headers = {"Content-Type": "application/json"}
    data = {"expression": expression}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")
        return None

# Example dice rolls
expressions = ["1d20+5", "2d6", "3d10+2", "4d8", "1d100"]

for expr in expressions:
    result = roll_dice(expr)
    if result:
        print(f"Expression: {expr}")
        print(f"Roll Result: {result['roll_result']}")
        print(f"GPT Response: {result['gpt_response']}\n")
