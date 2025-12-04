from flask import Flask, render_template_string, request
import json
import csv
import os

app = Flask(__name__)

# HTML Template
HTML_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
    <title>Products Display</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f5f5f5; }
        .container { max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; margin-bottom: 20px; border-bottom: 3px solid #4CAF50; padding-bottom: 10px; }
        .error { background: #ffebee; color: #c62828; padding: 15px; border-radius: 5px; margin: 20px 0; border: 1px solid #ffcdd2; }
        .info { background: #e3f2fd; color: #1565c0; padding: 15px; border-radius: 5px; margin: 20px 0; border: 1px solid #bbdefb; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th { background: #4CAF50; color: white; padding: 12px; text-align: left; }
        td { padding: 12px; border-bottom: 1px solid #ddd; }
        tr:hover { background: #f5f5f5; }
        .price { color: #2e7d32; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Products Display</h1>
        
        <div class="info">
            Source: <strong>{{ data_source }}</strong> | 
            Filter: <strong>{% if pid %}ID: {{ pid }}{% else %}All Products{% endif %}</strong> |
            Found: <strong>{{ products|length }} product(s)</strong>
        </div>
        
        {% if error %}
            <div class="error">
                <h3>Error</h3>
                <p>{{ error }}</p>
            </div>
        {% endif %}
        
        {% if products %}
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Category</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {% for product in products %}
                    <tr>
                        <td>{{ product.id }}</td>
                        <td>{{ product.name }}</td>
                        <td>{{ product.category }}</td>
                        <td class="price">${{ "%.2f"|format(product.price) }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% elif not error %}
            <div class="info">No products to display</div>
        {% endif %}
    </div>
</body>
</html>'''

# Veri dosyalarını oluştur
def create_data_files():
    # products.json zaten var (test dosyası)
    # products.csv oluştur
    if not os.path.exists('products.csv'):
        with open('products.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "category", "price"])
            writer.writerow([1, "Laptop", "Electronics", "799.99"])
            writer.writerow([2, "Coffee Mug", "Home Goods", "15.99"])
            writer.writerow([3, "Python Book", "Books", "39.99"])

# JSON dosyasını oku
def read_json_file():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except:
        return []

# CSV dosyasını oku
def read_csv_file():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except:
        return []

@app.route('/')
def home():
    return '<h1>Go to /products?source=json or /products?source=csv</h1>'

@app.route('/products')
def display_products():
    # Query parametrelerini al
    data_source = request.args.get('source', '').lower()
    pid = request.args.get('id', type=int)
    
    # CSV dosyasını oluştur (JSON zaten var)
    create_data_files()
    
    # Hata mesajı
    error = None
    products = []
    
    # Source kontrolü
    if data_source == 'json':
        products = read_json_file()
    elif data_source == 'csv':
        products = read_csv_file()
    else:
        error = "Wrong source. Use 'json' or 'csv'"
    
    # ID filtreleme
    if pid and not error:
        filtered = [p for p in products if p["id"] == pid]
        if filtered:
            products = filtered
        else:
            error = f"Product with ID {pid} not found"
    
    # Template'i render et (source yerine data_source kullan)
    return render_template_string(
        HTML_TEMPLATE,
        data_source=data_source,
        pid=pid,
        products=products,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
