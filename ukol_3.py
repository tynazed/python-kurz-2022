cena = 0

def over_cislo(cislo):
    cislo = cislo.replace(" ", "")
    if "+420" in cislo:
        if len(cislo[4:]) == 9:
            return True
        else:
            return False
    elif len(cislo) == 9:
        return True
    else:
        return False

def cena_sms(znaky: str):
    delka_sms = len(znaky)
    pocet_sms = int(delka_sms / 180)
    if delka_sms % 180 != 0:
        cena = (3 * pocet_sms) + 3
        return f"Cena SMS je {cena} Kč."
    else:
        cena = (3 * pocet_sms)
        return f"Cena SMS je {cena} Kč."

tel_cislo = input("Zadejte telefonní číslo: ")

overeni = over_cislo(tel_cislo)
print(overeni)

if overeni:
    sms = input("Zadejte zprávu: ")
    cena_za_sms = cena_sms(sms)
    print(cena_za_sms)
else:
    print("Zadali jste špatné číslo, proto nemůžete poslat SMS.")

