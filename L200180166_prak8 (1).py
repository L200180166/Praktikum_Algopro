##modul 8 
## kegiatan 2
def konversiSuhu (C = 0 , F = 0) :
    if C != 0 :
        x = (( 9 * C / 5 ) + 32)
        print ("Suhu", C , "Celcius setara dengan", x ,"Fahrenheit")
    elif F != 0 :
        y = (( F - 32) * 5 / 9 )
        print ("Suhu", F ,"Fahrenheit setara dengan", y ,"Celcius")
    else :
        print ("Suhu 0 Celcius setara dengan 32 Fahrenheit")
    return;
