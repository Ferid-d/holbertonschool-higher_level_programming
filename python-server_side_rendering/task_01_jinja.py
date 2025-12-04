from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Ana sayfa route'u"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Hakkımızda sayfası route'u"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """İletişim sayfası route'u"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
