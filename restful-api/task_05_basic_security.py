from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, create_refresh_token
)
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)

# Secret key for JWT - In production, use environment variable!
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-this'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hour

# Initialize authentication modules
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User database in memory
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1", 
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ========== BASIC AUTHENTICATION ==========

@auth.verify_password
def verify_password(username, password):
    """Basic authentication için password doğrulama"""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@auth.error_handler
def auth_error(status):
    """Basic auth hataları için"""
    return jsonify({"error": "Access denied"}), status

# ========== JWT ERROR HANDLERS ==========

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Token eksik veya yanlış header"""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Geçersiz token"""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Süresi dolmuş token"""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """İptal edilmiş token"""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Taze token gerekli"""
    return jsonify({"error": "Fresh token required"}), 401

# ========== ROLE-BASED ACCESS CONTROL DECORATOR ==========

def admin_required(fn):
    """Sadece admin kullanıcılar için decorator"""
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        if users.get(current_user, {}).get("role") != "admin":
            return jsonify({"error": "Admin access required"}), 403
        return fn(*args, **kwargs)
    return wrapper

# ========== ROUTES ==========

@app.route('/')
def home():
    """Ana sayfa"""
    return "Welcome to the Secure Flask API!"

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Basic authentication ile korunan route"""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """JWT token almak için login endpoint"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    
    # Kullanıcıyı kontrol et
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Password kontrol et
    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Token oluştur (username'i identity olarak ekle)
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    
    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    }), 200

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """JWT token ile korunan route"""
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@admin_required
def admin_only():
    """Sadece admin kullanıcılar için"""
    return "Admin Access: Granted"

# ========== ADDITIONAL ENDPOINTS ==========

@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Refresh token kullanarak yeni access token al"""
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_token}), 200

@app.route('/user-info', methods=['GET'])
@jwt_required()
def user_info():
    """Kullanıcı bilgilerini getir"""
    username = get_jwt_identity()
    user = users.get(username)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    # Password'ü gösterme
    user_info = {
        "username": user["username"],
        "role": user["role"]
    }
    
    return jsonify(user_info), 200

# ========== ERROR HANDLERS ==========

@app.errorhandler(404)
def not_found(error):
    """404 hataları"""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """500 hataları"""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
