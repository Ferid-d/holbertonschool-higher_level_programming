import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Basit API sunucusu için özel istek işleyici"""
    
    def do_GET(self):
        """GET isteklerini işler"""
        
        # Rota kontrolü
        if self.path == '/':
            self.handle_root()
        elif self.path == '/data':
            self.handle_data()
        elif self.path == '/status':
            self.handle_status()
        else:
            self.handle_not_found()
    
    def handle_root(self):
        """Ana sayfa için yanıt"""
        response_message = "Hello, this is a simple API!"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        self.wfile.write(response_message.encode('utf-8'))
    
    def handle_data(self):
        """JSON verisi döndürür"""
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        
        json_data = json.dumps(data)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        self.wfile.write(json_data.encode('utf-8'))
    
    def handle_status(self):
        """API durumunu döndürür"""
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        self.wfile.write(b"OK")
    
    def handle_not_found(self):
        """Tanımlanmamış endpoint'ler için 404 hatası"""
        error_message = "Endpoint not found"
        
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        self.wfile.write(error_message.encode('utf-8'))
    
    def log_message(self, format, *args):
        """Log mesajlarını gizle (isteğe bağlı)"""
        # Logları göstermek istemiyorsanız boş bırakın
        pass

def run_server(port=8000):
    """Sunucuyu başlatır"""
    handler = SimpleAPIHandler
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Server started on port {port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

if __name__ == "__main__":
    run_server(8000)
