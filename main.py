from flask import Flask, request, render_template
import morseConverter

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        conversion = request.form['conversion']
        wordToConvert = request.form['textinput']
        if conversion == '01':
            converted = morseConverter.encrypt(wordToConvert)
            return render_template('index.html', output=converted)
        elif conversion == '02':
            converted = morseConverter.decrypt(wordToConvert)
            return render_template('index.html', output=converted)


if __name__ == "__main__":
    app.run(debug=True)