vstupni_soubor = input("Zadejte název souboru: ")

with open(vstupni_soubor, encoding = "utf-8") as file:
    auta = file.readlines()

print(auta)

lines = [auto.split() for auto in auta]
print(lines)

lines = [[line[0], float(line[1].replace(",", "."))] for line in lines]
print(lines)

soucet_km = sum([line[1] for line in lines])
print(f"Auta celkem ujela {soucet_km} tisíc km.")
