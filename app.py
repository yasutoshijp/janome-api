from flask import Flask, request, jsonify
from janome.tokenizer import Tokenizer
import json

app = Flask(__name__)
tokenizer = Tokenizer()

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json(force=True)
    text = data.get('text', '')
    tokens = tokenizer.tokenize(text)
    result = [
        {
            'surface': token.surface,
            'part_of_speech': token.part_of_speech.split(','),
            'reading': token.reading,
            'base_form': token.base_form
        } for token in tokens
    ]
    return json.dumps(result, ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)