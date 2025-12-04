from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

# Template string olarak
ITEMS_HTML = '''<!doctype html>
<html lang="en">
<head><title>Items List</title></head>
<body>
    <h1>Items List</h1>
    {% if items %}
        <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No items found</p>
    {% endif %}
</body>
</html>'''

# items.json oluştur
if not os.path.exists('items.json'):
    with open('items.json', 'w') as f:
        json.dump({"items": ["Python Book", "Flask Mug", "Jinja Sticker"]}, f)

@app.route('/')
def home():
    return "Go to /items"

@app.route('/items')
def show_items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        items = data.get('items', [])
    except:
        items = []
    return render_template_string(ITEMS_HTML, items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
