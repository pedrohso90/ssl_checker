from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json
#some site without http/https in the path
base_url = 'www.google.com.br'
port = '443'
hostname = base_url
context = ssl.create_default_context()
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        data = json.dumps(ssock.getpeercert())
        # print(ssock.getpeercert())
print (data)
