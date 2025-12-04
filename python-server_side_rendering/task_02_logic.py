from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# items.json dosyasını oluştur
def create_items_file():
    """items.json dosyasını oluşturur veya kontrol eder"""
    if not os.path.exists('items.json'):
        with open('items.json', 'w') as f:
            json.dump({
                "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
            }, f, indent=2)

# Ana sayfa
@app.route('/')
def home():
    return "Go to /items to see the items list"

# Items sayfası
@app.route('/items')
def show_items():
    """Items listesini JSON'dan okuyup gösterir"""
    create_items_file()  # Dosya yoksa oluştur
    
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        items = data.get('items', [])
    except:
        items = []
    
    # Template'i render et
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
