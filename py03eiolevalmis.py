# 19.11.26 Nikita Ivtsenkov

# Ülesanne 3.7: Python Turtle Kolmnurk
import turtle
kylg = 200
nurk = 120
varv = "red"

turtle.color(varv)
for i in range(3):
    turtle.fd(kylg)
    turtle.left(nurk)
turtle.done()

# Ülesanne 3.5: Unistuse auto
auto_mark = "Toyota"
auto_mudel = "Supra Mk4"
auto = ("auto_mark" " + auto_mudel +")



# Ülesanne 3.3: Reisiplaan
sihtkoht = "Jaapan"
paevade_arv = 6
oobimise_hind = 45.60
print(sihtkoht,"reis kestab",paevade_arv,"päeva ja üks öö maksab ",oobimise_hind," eurot.")


# Ülesanne 3.2: Ostunimekiri
toode = "sussid"
kogus = 10
hind = 1.10
print("Soovin " + toode + " " + str(kogus) + ", mille tüki hind on "+str(hind)+" eurot.")

# Ülesanne 3.1: Tervitus
nimi = "Nikita"
vanus = 16
keskmine_hinne = 5.0
print(nimi,vanus,keskmine_hinne)
