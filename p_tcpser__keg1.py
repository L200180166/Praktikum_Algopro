# nama berkas: p_tcpser.py
# Tcp Server untuk Client p_tcplis.py

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50004))
s.listen(4)
print " program komunikasi tentang data diri  "
data = ''
kamus = {'nama' : 'Ahmad Fikri Alqhozali',
         'NIM' : ' L200180166 ',
         'angkatan' : 'angkatan 2018'}
while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        if data.lower() == 'keluar':
            s.close()
            break
        print ' Perintah :', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('maaf, perintah tidak dimngerti')
            
