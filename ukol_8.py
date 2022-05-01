from datetime import datetime

obdobi1_start = datetime(2021, 7, 1)
obdobi1_konec = datetime(2021, 8, 10)
cena_obdobi1 = 250

obdobi2_start = datetime(2021, 8, 11)
obdobi2_konec = datetime(2021, 8, 31)
cena_obdobi2 = 180

dotaz_datum_str = input("Na jaký den chcete koupit vstupenky? ")
dotaz_pocet_osob = int(input("Pro kolik osob chcete koupit vstupenky? "))

dotaz_datum = datetime.strptime(dotaz_datum_str.replace(" ", ""), "%d.%m.%Y")


if dotaz_datum >= obdobi1_start and dotaz_datum <= obdobi1_konec:
    celkova_cena = dotaz_pocet_osob * cena_obdobi1
    print(f"Cena za {dotaz_pocet_osob} osob pro datum {dotaz_datum_str} je {celkova_cena} Kč.")
elif dotaz_datum >= obdobi2_start and dotaz_datum <= obdobi2_konec:
    celkova_cena = dotaz_pocet_osob * cena_obdobi2
    print(f"Cena za {dotaz_pocet_osob} osob pro datum {dotaz_datum_str} je {celkova_cena} Kč.")
else:
    print("Letní kino je v této době uzavřené.")
