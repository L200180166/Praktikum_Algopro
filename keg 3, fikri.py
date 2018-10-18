Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Ahmad Fikri ALqhozali'
>>> NIM = 'L200180166'
>>> x = '1' NIM [7:]
SyntaxError: invalid syntax
>>> x = '1' NIM[7:]
SyntaxError: invalid syntax
>>> x = '1' + NIM[7:]
>>> a = int(x)
>>> b = len(nama)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b = len(nama)
NameError: name 'nama' is not defined
>>> b = len(nama)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b = len(nama)
NameError: name 'nama' is not defined
>>> b = len(Nama)
>>> type(a)
<type 'int'>
>>> type(b)
<type 'int'>
>>> a/b
55
>>> a//b
55
>>> 10* (a-999)
1670
>>> b**2
441
>>> a%b
11
>>> c = 12.5
>>> type(c)
<type 'float'>
>>> a/c
93.28
>>> a//c
93.0
>>> a%c
3.5
>>> c>b
False
>>> type(c>b)
<type 'bool'>
>>> a>b and b>c
True
>>> a>1000 or b<10
True
>>> 
