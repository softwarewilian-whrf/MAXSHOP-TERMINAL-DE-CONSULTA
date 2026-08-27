import http.server
import socketserver
import os

PORT = 8000
# Define o diretório atual do arquivo como raiz do servidor
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando em: http://localhost:{PORT}")
    httpd.serve_forever()