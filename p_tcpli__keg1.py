# nama berkas: p_tcpcli.py
# Client TCP untuk server p_tcpser.py

import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50004))
print " Program komunikasi Tentang diri "
while pesan.lower() != 'keluar':
    pesan = raw_input('perintah: ')
    s.send(pesan)
    if pesan.lower() != 'keluar':
        response =s.recv(1024)
        print 'jawab: ', response

    else :
        print 'SIAP!!!'
        s.close()
