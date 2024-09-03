  GNU nano 8.1                                                                                                     routes.py                                                                                                      Modified
print("Welcome to the Dice Roller Project!")
from flask import Flask, jsonify, request
import d20

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the D&D Dice nano routes.py
from flask import Flask, jsonify, request
import d20

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the D&D Dice Roller!"

@app.route('/roll')
def roll_dice():
    dice_expression = request.args.get('expression', 'd20')
    roll = d20.roll(dice_expression)
    return jsonify({
        "expression": dice_expression,
        "result": str(roll),  # Convert roll to string to handle dice roll objects
        "total": roll.total
    })

if __name__ == '__main__':
    app.run(debug=True)
def roll_dice():
    dice_expression = request.args.get('expression', 'd20')
    roll = d20.roll(dice_expression)
    return jsonify({
        "expression": dice_expression,
        "result": str(roll),  # Convert roll to string to handle dice roll objects
        "total": roll.total
    })

if __name__ == '__main__':
    app.run(debug=True)
flask run




print("Welcome to the Dice Roller Project!")
from flask import Flask, jsonify, request
import d20

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the D&D Dice nano routes.py
from flask import Flask, jsonify, request
import d20

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the D&D Dice Roller!"

@app.route('/roll')
def roll_dice():
    dice_expression = request.args.get('expression', 'd20')
    roll = d20.roll(dice_expression)
    return jsonify({
        "expression": dice_expression,
        "result": str(roll),  # Convert roll to string to handle dice roll objects
        "total": roll.total
    })

if __name__ == '__main__':
    app.run(debug=True)
def roll_dice():
    dice_expression = request.args.get('expression', 'd20')
    roll = d20.roll(dice_expression)
    return jsonify({
        "expression": dice_expression,
        "result": str(roll),  # Convert roll to string to handle dice roll objects
        "total": roll.total
    })

if __name__ == '__main__':
    app.run(debug=True)
flask run



