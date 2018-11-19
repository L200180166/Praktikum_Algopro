a = {'NIM':'L200180166','Nama':'Ahmad fikri Alqhozali','Alamat':'bekasi','Panggilan':'fikri','PT':'UMS','Fak':'FKI','Prodi':'Informatika'}

print "Pilihan yang tersedia:"
print "N menampilkan Nama"
print "n menampilkan NIM"
print "l menampilkan Alamat"
print "p menampilkan Panggilan"
print "t menampilkan PT"
print "f menampilkan Fakultas"
print "i menampilkan Prodi"


def Nama():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Nama:' + a['Nama']
    

def NIM():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'NIM:' + a['NIM']
    
def Alamat():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Alamat:' + a['Alamat']
    
def Panggilan():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Panggilan:' + a['Panggilan']

def PT():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'PT:' + a['PT']
    
def Fak():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Fakultas:' + a['Fak']
    
def Prodi():
    "menampilkan data diri masing-masing 1 setiap data"
    print 'Prodi:' + a['Prodi']


repeat = True

while repeat :
    x = raw_input("Pilihan Saudara :")
    if x == "N" :
        Nama()
    elif x == "n" :
        NIM()
    elif x == "l" :
        Alamat()
    elif x == "p" :
        Panggilan()
    elif x == "t" :
        PT()
    elif x == "f" :
        Fak()
    elif x == "i" :
        Prodi()
    elif x == "k" :
        print "Terima Kasih."
        repeat = False
