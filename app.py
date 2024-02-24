
from flask import Flask, request, render_template, jsonify
from check_syllable import check_syllable
from check_word import check_word
from Japanese to Hiragana import latin_to_hiragana
from english_translation import hiragana_english

app = Flask(__name__)

# ... (Other imports and code)

# Route for handling Function 1 form submission
@app.route('/result_function1', methods=['POST'])
def result_function1():
    syllable = request.form.get('function1Input')
    result = check_syllable(syllable)
    return jsonify({'result': result})

# Route for handling Function 2 form submission
@app.route('/result_function2', methods=['POST'])
def result_function2():
    word = request.form.get('function2Input')
    result = check_word(word)
    return jsonify({'result': result})

# Route for handling Function 3 form submission
@app.route('/result_function3', methods=['POST'])
def result_function3():
    jpword = request.form.get('function3Input')
    hiragana_version = latin_to_hiragana(jpword)
    return jsonify({'hiragana_version': hiragana_version})

# Route for handling Function 4 form submission
@app.route('/result_function4', methods=['POST'])
def result_function4():
    jpword = request.form.get('function4Input')
    hiragana_and_english = hiragana_english(jpword)
    return jsonify({'hiragana_and_english': hiragana_and_english})

# ... (Other routes and code)

if __name__ == '__main__':
    app.run(debug=True)
