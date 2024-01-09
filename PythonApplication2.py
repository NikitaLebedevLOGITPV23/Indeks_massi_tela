
#13
try:
    gender=input("Sugu: ")
    if gender.isaaplha() and (gender.lower()=="naine" or gender.lower()=="mees"):
        if gender.lower()=="naine":
            print("Ei soobi")
            else:
        try:
            age=int(input("Vanus: "))
            if 16<=age<=18:
                print("Oled meeskonnas!")
            else:
            
                print("Vanus ei soobi!")
        except :
            print("Vale banus! Viga andmetüübiga!")
    else:
        print("Sisesta õige tekst!")
except :
    print("Viga andmetüübiga")




gender=input("Kas sa oled mees või naine?")
if gender.lower()=="naine":
    print("Kahjuks, otsime ainult mehi")
else:
    age=int(input("Palun markige oma vanus"))
    if age>16 and age <18:
        print("Sa sobib mie meeskonda!")
    else:
        print("Kahjuks sa ei sobi meeskonda.")

#12
hind = float(input("Sisesta toote hind: "))
if hind <= 10:
    soodustus = hind * 0.1
else:
    soodustus = hind * 0.2
    okonnelik_hind = hind - soodustus
    print("Lõplik hind on", okonnelik_hind, "€")


#9
try:
    s1 = float(input("Введите длину первой стороны квадрата "))
    s2 = float(input("Введите длину второй стороны квадрата "))

    if s1 == s2:
        print("Это квадрат!")
    else: print("Это не квадрат.")
except :
    print("Где-то ошибка посмотрите тип как вы указали данные!")

a=10 #int
b=2.3 #float
c="programma" #str
d="progal" #str
d="2.1" #str
print(b.is_integer()) #false
print(a.is_integer()) #false
print(c.isalpha()) #true
print(a.isalpha()) #false
print(a.isnumeric()) #false
print(a.isdigit()) #false
print(a.isdecimal()) #false

print("Tere! Olen sinu uus sõber — Python!")
nimi=input("Mis on sinu nimi on?")
print(nimi,",oi kui ilus nimi!")
indeks=input(nimi+"Kas leian Sinu keha indeksi? 0-ei, 1-jah=")
if indeks=="1":
    pikkus=int(input(nimi+",Sinu pikkus(cm=>)"))
    mass=float(input())
    indeks=mass/(0.01*pikkus)**2
    print(nimi+"!Sinu keha indeks on:",round(indeks,2))
    if indeks<16:
        print("Tervisele ohtlik alakaal")
    elif 16<indeks<19:
             print("Alakaal")
    elif 19<indeks<25:
        print("Normaalkaal")
    elif 25<indeks<30:
        print("Ülekaal")
    elif 30<indeks<35:
        print("Rasvumine")
    elif 35<indeks<40:
        print("Tugev rasvumine")
    elif 40>indeks:
        print("Tervisele ohtlik rasvamine")
    elif indeks=="0":
