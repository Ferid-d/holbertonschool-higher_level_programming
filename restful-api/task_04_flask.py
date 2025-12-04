from flask import Flask, jsonify, request

app = Flask(__name__)

# Kullanıcı veritabanı (memory'de tutulacak)
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    """Ana sayfa"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Tüm kullanıcı adlarını döndürür"""
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status')
def get_status():
    """API durumunu döndürür"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Belirtilen kullanıcıyı döndürür"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Yeni kullanıcı ekler"""
    
    # JSON verisini kontrol et
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    
    # Username kontrolü
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    
    # Kullanıcı zaten var mı?
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Yeni kullanıcı oluştur
    new_user = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }
    
    # Kullanıcıyı ekle
    users[username] = new_user
    
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
