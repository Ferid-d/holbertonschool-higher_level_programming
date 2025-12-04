from flask import Flask, render_template_string, request
import json
import csv
import sqlite3
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

# Veritabanını oluştur
def create_database():
    if not os.path.exists('products.db'):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99),
            (3, 'Python Book', 'Books', 39.99),
            (4, 'Headphones', 'Electronics', 129.99)
        ''')
        conn.commit()
        conn.close()

# CSV dosyasını oluştur
def create_csv_file():
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

# SQLite veritabanından oku
def read_sql_database():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        
        conn.close()
        return products
    except:
        return []

@app.route('/')
def home():
    return '<h1>Go to /products?source=json or /products?source=csv or /products?source=sql</h1>'

@app.route('/products')
def display_products():
    # Query parametrelerini al
    data_source = request.args.get('source', '').lower()
    pid = request.args.get('id', type=int)
    
    # Dosyaları oluştur
    create_database()   # SQLite DB
    create_csv_file()   # CSV
    
    # Hata mesajı
    error = None
    products = []
    
    # Source kontrolü
    if data_source == 'json':
        products = read_json_file()
    elif data_source == 'csv':
        products = read_csv_file()
    elif data_source == 'sql':
        products = read_sql_database()
    else:
        error = "Wrong source"
    
    # ID filtreleme
    if pid and not error:
        filtered = [p for p in products if p["id"] == pid]
        if filtered:
            products = filtered
        else:
            error = "Product not found"
    
    # Template'i render et
    return render_template_string(
        HTML_TEMPLATE,
        products=products,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
