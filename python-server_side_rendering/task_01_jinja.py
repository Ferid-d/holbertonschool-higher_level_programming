from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML template'leri string olarak tanımla
index_html = '''
<!doctype html>
<html lang="en">
<head>
    <title>My Flask App</title>
</head>
<body>
    <header>
        <h1>My Flask App</h1>
        <nav>
            <a href="/">Home</a> | 
            <a href="/about">About</a> | 
            <a href="/contact">Contact</a>
        </nav>
    </header>
    
    <main>
        <h1>Welcome to My Flask App</h1>
        <p>This is a simple Flask application.</p>
        <ul>
            <li>Flask</li>
            <li>HTML</li>
            <li>Templates</li>
        </ul>
    </main>
    
    <footer>
        <p>&copy; 2024 My Flask App</p>
    </footer>
</body>
</html>
'''

about_html = '''
<!doctype html>
<html lang="en">
<head>
    <title>About - My Flask App</title>
</head>
<body>
    <header>
        <h1>My Flask App</h1>
        <nav>
            <a href="/">Home</a> | 
            <a href="/about">About</a> | 
            <a href="/contact">Contact</a>
        </nav>
    </header>
    
    <main>
        <h1>About Us</h1>
        <p>This is the about page for My Flask App.</p>
    </main>
    
    <footer>
        <p>&copy; 2024 My Flask App</p>
    </footer>
</body>
</html>
'''

contact_html = '''
<!doctype html>
<html lang="en">
<head>
    <title>Contact - My Flask App</title>
</head>
<body>
    <header>
        <h1>My Flask App</h1>
        <nav>
            <a href="/">Home</a> | 
            <a href="/about">About</a> | 
            <a href="/contact">Contact</a>
        </nav>
    </header>
    
    <main>
        <h1>Contact Us</h1>
        <p>This is the contact page for My Flask App.</p>
    </main>
    
    <footer>
        <p>&copy; 2024 My Flask App</p>
    </footer>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(index_html)

@app.route('/about')
def about():
    return render_template_string(about_html)

@app.route('/contact')
def contact():
    return render_template_string(contact_html)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
