def hitung():
    "Untuk menghitung luas Jajargenjang"
    s = a * t
    return s
print "<!DOCTYPE html>"
print
print """<html>
    <head><title> Menghitung luas bangun Geometri</title></head>
    <body>"""
a = 5
t = 10
print """<table>
    <tr>
        <td rowspan="7">FOTO</td>
        <td><center>Bangun Geometri</center></td>
    </tr>
     <tr>
        <td> Nama Bangun </td>
    </tr>
     <tr>
        <td> Dimensi (2D / 3D )</td>
    </tr>
    <tr>
        <td> Rumus luas : Alas x Tinggi</td>
    </tr>
     <tr>
        <td> Parameter 1 </td>
    </tr>
     <tr>
        <td> Parameter 2 </td>
    </tr>
    <tr>
        <td> Luas : """.format(a, t)
print hitung(), """</td>

    </tr></table></body>"""
print "</html>"
