baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod = input("Jaký je kód vašeho balíku? ")

if baliky[kod] is True:
    print("Balík byl předán kurýrovi.")
else:
    print("Balík zatím nebyl předán kurýrovi.")