Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Ahmad Fikri Alqhozali'
>>> NIM = 166
>>> Tinggi = 1.73
>>> Berat = 55
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<type 'tuple'>
>>> Aku[0]
2000
>>> a = NIM % 4; Aku[a]
1.73
>>> type (Aku[a])
<type 'float'>
>>> Aku[a:4]
(1.73, 166)
>>> type(Aku[4])
<type 'str'>
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> type(Data)
<type 'list'>
>>> type(Data[4])
<type 'str'>
>>> Data [4][5]
' '
>>> Data [4][a:6]
'mad '
>>> Data [0] = 'ok' ; Data
['ok', 55, 1.73, 166, 'Ahmad Fikri Alqhozali']
>>> Data [-a]
166
>>> range(a)
[0, 1]
>>> 
