vstupni_soubor = input("Zadejte název souboru: ")

with open(vstupni_soubor, encoding = "utf-8") as file:
    auta = file.readlines()

print(auta)

lines = [auto.split() for auto in auta]
print(lines)

lines = [[line[0], float(line[1].replace(",", "."))] for line in lines]
print(lines)

seznam_km = []
seznam_km = [line[1] for line in lines]
print(seznam_km)

soucet_km = sum(seznam_km)
print(f"Auta celkem ujela {soucet_km} tisíc km.")
