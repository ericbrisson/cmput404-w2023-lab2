import socket

# set to ~4kb because that's a nice amount to receive in a packet uninterrupted
BYTES_TO_READ = 4096

def get(host, port):
    # created our request
    request_data = b'GET / HTTP/1.1\nHost:' + host.encode('utf-8') + b'\n\n'
    
    # created our socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # we've sent some data on our socket
    s.connect((host, port))
    s.send(request_data)
    s.shutdown(socket.SHUT_WR)

    # listen for response
    response = s.recv(BYTES_TO_READ)
    print(response)
    while(len(response) > 0):
        print(response)
        response = s.recv(BYTES_TO_READ)

    # close socket once done with it
    s.close()

get("www.google.com", 80)