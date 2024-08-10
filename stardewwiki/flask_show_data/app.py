from flask import Flask, render_template, jsonify
from pathlib import Path
import json


app = Flask(__name__)

# 获取 static 文件夹的绝对路径
static_folder = Path(app.root_path) / 'static'

# 获取所有图片文件
image_files = [file.name for file in static_folder.glob('*.png')]

def load_data():
    with open(r'./stardewwiki/flask_show_data/results_bundle.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/imgs')
def show_images():
    return render_template('imgs.html', image_files=image_files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
