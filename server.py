from socket import (
    socket, 
    AF_INET, 
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)
import python_http_parser
import yaml
from handler import Handler

#get config file settings
with open('config.yaml') as config:
    configs = yaml.safe_load(config) 

HOST, PORT = configs['address'],configs['port']

response =  b"HTTP/1.1 200 OK\n\nHello World"


with socket(AF_INET, SOCK_STREAM) as sock:
    #open socket using config file settings
    print(f'Listening on: {HOST}:{PORT}')
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(10)
    while True:
        try:
            #start receiving requests
            conn, addr = sock.accept()
            req = conn.recv(1024).decode()
            req = python_http_parser.parse(req)
           
            #pass request to handler
            res = Handler.start_response(req["req_uri"])
            
            #return response
            conn.sendall(res)
            conn.close()
        except Exception as E:
            print(E)
            conn.close()