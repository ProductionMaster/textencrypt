from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of symbols to use in encryption
symbols = ["\"", "'", "/", "&", "!", "@", "#", "$", "%", "^", "(", "*", ")", ",", ".", "|", "}", "{", " "]

# Function to generate a random symbol
def GenRandomSymbol():
    return random.choice(symbols)

# Function to encrypt a string
def Encrypt(String):
    String = String[::-1]  # Reverse the string
    encrypted_string = []
    for char in String:
        random_symbol1 = GenRandomSymbol()
        random_symbol2 = GenRandomSymbol()
        encrypted_string.append(f"{random_symbol1}{char}{random_symbol2}")  # Insert symbols around the character
    return "".join(encrypted_string)

# Function to decode an encrypted string
def Decode(encrypted_string):
    decoded_string = []
    i = 0
    while i < len(encrypted_string):
        if encrypted_string[i] in symbols:
            i += 1  # Skip the first random symbol
            char = encrypted_string[i]
            decoded_string.append(char)  # Add the character to the decoded string
            i += 1  # Skip the second random symbol
        i += 1
    return "".join(decoded_string[::-1])  # Reverse the decoded string

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        text = request.form.get('text')
        if action == 'Encrypt':
            result = Encrypt(text)
        elif action == 'Decode':
            result = Decode(text)
        else:
            result = "Invalid action"
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
