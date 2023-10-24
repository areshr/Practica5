import http.server
import socketserver
import json
import random

# Datos ficticios de clima 
paises = {
    "China" : {"temperatura": random.uniform(25, 30), "clima":"Soleado"},
    "Brasil": {"temperatura": random.uniform(25, 30), "clima":"Parcialmente_nublado"},
    "France": {"temperatura": random.uniform(9, 15), "clima":"Nublado"},
    "Japan": {"temperatura": random.uniform(6, 17), "clima":"Mayormente_nublado"},
    "Mexico": {"temperatura": random.uniform(14, 27), "clima":"Parcialmente_nublado"},
    "Canada": {"temperatura": random.uniform(3, 8), "clima":"Despejado_con_intervalos_nublosos"},
    "USA": {"temperatura": random.uniform(7, 16), "clima":"Mayormente_nublado"},
    "England": {"temperatura": random.uniform(8, 16), "clima":"Nublado"},
}

# Datos de listas de reproducción de Spotify
listasReproducion ={
    "China": {"listas": ["China_Mix", "Éxitos_China", "TOP_China"]},
    "Brasil": {"listas": ["Brasil_Mix", "Éxitos_Brasil", "TOP_Brasil"]},
    "France": {"listas": ["France_Mix", "Éxitos_France", "TOP_France"]},
    "Japan": {"listas": ["Colombia_Japan", "Éxitos_Japan", "TOP_Japan"]},
    "Mexico": {"listas": ["México_Mix", "Éxitos_México", "TOP_México"]},
    "Canada": {"listas": ["Canada_Mix", "Éxitos_Canada", "TOP_Canada"]},
    "USA": {"listas": ["USA_Mix", "Éxitos_USA", "TOP_USA"]},
    "England": {"listas": ["England_Mix", "Éxitos_England", "TOP_England"]},
}

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/temperature/'):
            pais = self.path[13:]
            if pais in paises:
                data = {"pais": pais, "temperatura": paises[pais]["temperatura"], "clima": paises[pais]["clima"]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())

        elif self.path.startswith('/playlist/'):
            pais = self.path[10:]
            if pais in listasReproducion:
                data = {"pais": pais, "listas": listasReproducion[pais]["listas"]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())

        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor en el puerto 9090")
    httpd.serve_forever()

