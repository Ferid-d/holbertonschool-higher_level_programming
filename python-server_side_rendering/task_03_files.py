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
</head>
<body>
    <h1>Products Display</h1>
    
    {% if error %}
        <p style="color: red;"><strong>Error:</strong> {{ error }}</p>
    {% endif %}
    
    {% if products %}
        <table border="1">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Category</th>
                <th>Price</th>
            </tr>
            {% for product in products %}
            <tr>
                <td>{{ product.id }}</td>
                <td>{{ product.name }}</td>
                <td>{{ product.category }}</td>
                <td>${{ "%.2f"|format(product.price) }}</td>
            </tr>
            {% endfor %}
        </table>
    {% elif not error %}
        <p>No products to display</p>
    {% endif %}
</body>
</html>'''

# Veri dosyalarını oluştur
def create_data_files():
    # products.csv oluştur
    if not os.path.exists('products.csv'):
        with open('products.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "category", "price"])
            writer.writerow([1, "Laptop", "Electronics", "799.99"])
            writer.writerow([2, "Coffee Mug", "Home Goods", "15.99"])

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
    
    # CSV dosyasını oluştur
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
        error = "Wrong source"
    
    # ID filtreleme - TEST İÇİN TAM "Product not found" MESAJI
    if pid and not error:
        filtered = [p for p in products if p["id"] == pid]
        if filtered:
            products = filtered
        else:
            error = "Product not found"  # Tam olarak bu mesaj
    
    # Template'i render et
    return render_template_string(
        HTML_TEMPLATE,
        products=products,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
