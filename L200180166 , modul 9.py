#/usr/bin/python
# menulis data ke dalam berkas
#kegiatan 1 
##berkas = open("L200180166.txt", "w")
##berkas.write(" NIM=L200180166 \n")
##berkas.write(" TL=06-06-2000 \n")
##berkas.write(" Nama=Ahmad Fikri Alqhozali \n")
##berkas.close()
##

###KEGIATAN 2

##berkas = open("L200180166.txt", "w")
##berkas.write(" NIM = L200180166 \n")
##berkas.write(" TL = 06-06-2000 \n")
##berkas.write(" Nama = Ahmad Fikri Alqhozali \n")
##berkas.write("Kotalahir = Jakarta ")
##berkas.close()
##z = open ("L200180166.txt", "r")
##NIM = z.readline()
##TL = z.readline()
##Nama = z.readline()
##Kotalhr = z.readline()
##print Nama
##print Kotalhr, TL
##print NIM
##

#####KEGIATAN 3

####import shelve
####a = open ("L200180166.txt", "r")
####NIM = a.readline()
####TL = a.readline()
####Nama = a.readline()
####a.close()
####
####a=shelve.open("fikri")
####a['b'] = [NIM, TL, Nama]
####a.close()
##

#####KEGIATAN 4

####a=shelve.open("fikri")
####print a['b']
####print a['b'][0]
####print a['b'][1]
####print a['b'][2]
