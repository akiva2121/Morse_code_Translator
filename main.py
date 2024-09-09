from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

# Morse code dictionary
morse_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--",
    "?": "..--..", "!": "-.-.--", "=": "-...-", " ": "/"
}


# Function to convert text to Morse code
def text_to_morse(text):
    return ' '.join(morse_dict.get(char.upper(), '') for char in text)


# Function to convert Morse code to text
def morse_to_text(morse):
    reverse_dict = {v: k for k, v in morse_dict.items()}
    return ''.join(reverse_dict.get(code, '') for code in morse.split())


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        direction = request.form['direction']
        message = request.form['message']

        if direction == 'to_code':
            # Convert text to Morse code
            result = text_to_morse(message)
        elif direction == 'to_english':
            # Convert Morse code to text
            result = morse_to_text(message)
        else:
            result = "Invalid direction"

        return render_template("index.html", result=result)

    return render_template("index.html", result="")


if __name__ == "__main__":
    app.run(debug=True)


