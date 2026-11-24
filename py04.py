# 19.11.26 Nikita Ivtsenkov

# Ringi pindala ja Turtle
# Kirjuta programm, mis kasutab Turtle graafikat joonistamaks ringi ning arvutab ja kuvab konsoolis ringi pindala ja ümbermõõdu.
import turtle
try:
    r = int(input("Sisesta raadius: "))
    S = 3.14 * r ** 2
    C = 2 * 3.14 * r
    turtle.circle(r)
    print(s, p)
    turtle.done()
except ValueError:
    print("urror")



# Faili allalaadimine
# Kirjuta programm, mis aitab arvutada, kui kaua kulub aega faili allalaadimiseks.
try:
    suurus = int(input("Sisesta suurus MB: "))
    kiirus = int(input("Sisesta kiirus MB/s: "))
    if kiirus == 0:
        print("Nulliga ei saa jagada")
    else:
        vastus = suurus / kiirus

    print(int(vastus))
except ValueError:
    print("Mingi jama")


# Aia pikkus
# Kirjuta programm, mis aitab aiapidajal arvutada aia ümbermõõtu.
x = int(input("Sisesta külg 1: "))
y = int(input("Sisesta külg 2: "))
pikkus = (x + y) * 2

print(f"Aia kogupikkus on {pikkus} meetrit.")
























