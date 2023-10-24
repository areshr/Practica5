import http.server
import socketserver
import json
import random

# Datos ficticios de canciones para una lista de reproducción de Spotify
canciones = [
    {"nombre": "The Hills", "artista": "The Weeknd", "duracion": "4:02"},
    {"nombre": "breathin", "artista": "Ariana Grande", "duracion": "3:18"},
    {"nombre": "pa querert", "artista": "Rels B", "duracion": "4:03"},
    {"nombre": "Perro Negro", "artista": "Bad Bunny, Feid", "duracion": "2:42"},
    {"nombre": "Julieta", "artista": "LATIN MAFIA", "duracion": "3:30"},
]

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/playlist':
            data = {"canciones": canciones}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Ruta no encontrada.".encode())

# Configuración del servidor
with socketserver.TCPServer(("", 9092), MyHandler) as httpd:
    print("Servidor de lista de reproducción en el puerto 9092")
    httpd.serve_forever()
