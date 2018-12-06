import socket
def jajargenjang(s=0):
    return s*s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50006))
s.listen(5)
print "Server penghitung otomatis sudah siap"
data = ''
while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() !='keluar':
        data = komm.recv(1024)
        print 'Pesan:', data
        if data.find("parameter")!= -1:
            param,value= data.split("=")
            if param == "parameter sisi":
                s=float(value)
                b=value
                komm.send("parameter dicatat")
        elif data=='hitung':
            komm.send('luas jajargenjang dengan sisi {} adalah {}'.format (b,jajargenjang(s)))
        else:
            komm.send('tidak ada')
