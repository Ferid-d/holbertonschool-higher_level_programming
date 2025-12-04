from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

# HTML template for items page
items_html = '''
<!doctype html>
<html lang="en">
<head>
    <title>Items List</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }
        body {
            background-color: #f5f5f5;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        header {
            background: #4CAF50;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 8px 8px 0 0;
            margin-bottom: 20px;
        }
        h1 {
            margin-bottom: 10px;
        }
        nav {
            margin-bottom: 20px;
            text-align: center;
        }
        nav a {
            color: #4CAF50;
            text-decoration: none;
            margin: 0 10px;
            padding: 5px 10px;
            border-radius: 4px;
        }
        nav a:hover {
            background-color: #f0f0f0;
        }
        .items-list {
            list-style-type: none;
            padding: 0;
        }
        .item {
            background: #f9f9f9;
            padding: 15px;
            margin: 10px 0;
            border-left: 5px solid #4CAF50;
            border-radius: 4px;
            display: flex;
            align-items: center;
        }
        .item-number {
            background: #4CAF50;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
            font-weight: bold;
        }
        .no-items {
            background: #ffebee;
            padding: 20px;
            text-align: center;
            border-radius: 8px;
            color: #c62828;
            border: 1px solid #ffcdd2;
        }
        footer {
            margin-top: 30px;
            text-align: center;
            color: #666;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }
        .json-content {
            background: #f5f5f5;
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
            font-family: monospace;
            white-space: pre-wrap;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>My Flask App</h1>
            <p>Dynamic Items List with Jinja</p>
        </header>
        
        <nav>
            <a href="/">Home</a> | 
            <a href="/about">About</a> | 
            <a href="/contact">Contact</a> | 
            <a href="/items">Items</a>
        </nav>
        
        <h2>Items List</h2>
        
        {% if items %}
            <p>Found {{ items|length }} item(s):</p>
            <ul class="items-list">
                {% for item in items %}
                <li class="item">
                    <div class="item-number">{{ loop.index }}</div>
                    <div>
                        <strong>{{ item }}</strong>
                        <div style="font-size: 12px; color: #666; margin-top: 5px;">
                            Index: {{ loop.index0 }} | 
                            {% if loop.first %}First item | {% endif %}
                            {% if loop.last %}Last item{% endif %}
                        </div>
                    </div>
                </li>
                {% endfor %}
            </ul>
        {% else %}
            <div class="no-items">
                <h3>No items found</h3>
                <p>The items list is empty. Please add some items to the JSON file.</p>
            </div>
        {% endif %}
        
        <div class="json-content">
            <strong>Loaded from JSON:</strong><br>
            {{ json_data }}
        </div>
        
        <footer>
            <p>&copy; 2024 My Flask App</p>
            <p style="font-size: 12px; margin-top: 5px;">
                Template rendered at: {{ timestamp }}
            </p>
        </footer>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return "Welcome to Flask Dynamic Template App! Go to /items"

@app.route('/items')
def show_items():
    """Display items from JSON file"""
    try:
        # Read JSON data from file
        with open('items.json', 'r') as f:
            data = json.load(f)
        
        items = data.get('items', [])
        json_str = json.dumps(data, indent=2)
        
    except FileNotFoundError:
        # If file doesn't exist, use default data
        items = ["Python Book", "Flask Mug", "Jinja Sticker", "Web Dev Guide"]
        json_str = json.dumps({"items": items}, indent=2)
        
        # Create the JSON file for next time
        with open('items.json', 'w') as f:
            json.dump({"items": items}, f, indent=2)
    
    except json.JSONDecodeError:
        items = []
        json_str = "Error: Invalid JSON format in items.json"
    
    # Render template with data
    return render_template_string(
        items_html,
        items=items,
        json_data=json_str,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

# Create items.json file if it doesn't exist
if not os.path.exists('items.json'):
    with open('items.json', 'w') as f:
        json.dump({
            "items": [
                "Python Book", 
                "Flask Mug", 
                "Jinja Sticker",
                "Web Development Guide",
                "API Documentation",
                "Tutorial Videos"
            ]
        }, f, indent=2)

if __name__ == '__main__':
    from datetime import datetime
    app.run(debug=True, port=5000)
