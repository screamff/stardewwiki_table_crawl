from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_data():
    with open(r'./stardewwiki/flask_show_data/results_bundle.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
