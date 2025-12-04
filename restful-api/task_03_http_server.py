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
        elif self.path == '/info':
            self.handle_info()
        else:
            self.handle_not_found()
    
    def handle_root(self):
        """Ana sayfa için yanıt"""
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        response_message = "Hello, this is a simple API!"
        self.wfile.write(response_message.encode('utf-8'))
    
    def handle_data(self):
        """JSON verisi döndürür"""
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        
        json_data = json.dumps(data, indent=2)
        self.wfile.write(json_data.encode('utf-8'))
    
    def handle_status(self):
        """API durumunu döndürür"""
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        self.wfile.write(b"OK")
    
    def handle_info(self):
        """API bilgilerini döndürür"""
        info = {
            "version": "1.0",
            "description": "A simple API built with http.server",
            "endpoints": {
                "/": "Welcome message",
                "/data": "Sample JSON data",
                "/status": "API status",
                "/info": "API information"
            }
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        
        json_info = json.dumps(info, indent=2)
        self.wfile.write(json_info.encode('utf-8'))
    
    def handle_not_found(self):
        """Tanımlanmamış endpoint'ler için 404 hatası"""
        error_message = {
            "error": "Endpoint not found",
            "message": f"The requested endpoint '{self.path}' does not exist",
            "available_endpoints": ["/", "/data", "/status", "/info"]
        }
        
        self.send_response(404)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        
        json_error = json.dumps(error_message, indent=2)
        self.wfile.write(json_error.encode('utf-8'))
    
    def log_message(self, format, *args):
        """Log mesajlarını özelleştir (isteğe bağlı)"""
        print(f"[{self.address_string()}] {args[0].split()[0]} {self.path}")

def run_server(port=8000):
    """Sunucuyu başlatır"""
    handler = SimpleAPIHandler
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🚀 Server started on http://localhost:{port}")
        print(f"📡 Available endpoints:")
        print(f"   • http://localhost:{port}/")
        print(f"   • http://localhost:{port}/data")
        print(f"   • http://localhost:{port}/status")
        print(f"   • http://localhost:{port}/info")
        print("\n📝 Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped")
            httpd.shutdown()

if __name__ == "__main__":
    run_server(8000)
