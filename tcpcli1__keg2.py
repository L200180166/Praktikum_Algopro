import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50008))
print " program kmounikasi tentang server "
while pesan.lower() !='quit':
    pesan = raw_input('command: ')
    s.send(pesan)
    if pesan.lower() !='quit':
        response = s.recv(1024)
        print 'response', response
    else:
        s.close()
