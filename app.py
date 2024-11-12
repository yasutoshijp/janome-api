from flask import Flask, request, jsonify
from janome.tokenizer import Tokenizer
import json
import os

app = Flask(__name__)
tokenizer = Tokenizer()

@app.route('/analyze', methods=['POST'])
def analyze_post():
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

@app.route('/api/analyze', methods=['GET'])
def analyze_get():
    text = request.args.get('text', '')
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
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)