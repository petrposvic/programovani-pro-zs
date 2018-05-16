class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def s(self):
        return self.a * self.b

    def o(self):
        return 2 * self.a + 2 * self.b

class Circle:
    def __init__(self, r):
        self.r = r

    def s(self):
        return 3.14 * self.r * self.r

    def o(self):
        return 2 * 3.14 * self.r

print("+------------+")
print("| Kalkulator |")
print("+------------+")

def basics():
    a = input("Zadej prvni cislo: ")
    b = input("Zadej druhe cislo: ")
    o = input("Zadej operaci (+ - * /): ")

    print("Vysledek je: ", end="")
    if (o == "+"):
        print(float(a) + float(b))

    if (o == "-"):
        print(float(a) - float(b))

    if (o == "*"):
        print(float(a) * float(b))

    if (o == "/"):
        print(float(a) / float(b))

def formulas():
    while True:
        print("a) obdelnik")
        print("b) kruh")
        print("c) zpet")
        i = input()

        if (i == "a"):
            a = float(input("Zadej delku strany A: "))
            b = float(input("Zadej delku strany B: "))
            z = Rect(a, b)
            print("a) obsah")
            print("b) obvod")
            j = input()
            if (j == "a"):
                print("Obsah obdelniku o stranach {}x{} je {}".format(a, b, z.s()))
            if (j == "b"):
                print("Obvod obdelniku o stranach {}x{} je {}".format(a, b, z.o()))

        if (i == "b"):
            r = float(input("Zadej polomer: "))
            z = Circle(r)
            print("a) obsah")
            print("b) obvod")
            j = input()
            if (j == "a"):
                print("Obsah kruhu o polomeru {} je {}".format(r, z.s()))
            if (j == "b"):
                print("Obvod kruhu o polomeru {} je {}".format(r, z.o()))

        if (i == "c"):
            break
    
while True:
    print()
    print("Co chces udelat?")
    print("a) zakladni operace")
    print("b) vzorecky")
    print("c) konec")
    i = input()

    if (i == "a"):
        basics()

    if (i == "b"):
        formulas()

    if (i == "c"):
        break

print("Konec programu")
