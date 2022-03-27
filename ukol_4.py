class Auto:
    def __init__(self, registr_znacka, znacka_auta, typ_auta, pocet_km):
        self.registr_znacka = registr_znacka
        self.znacka_auta = znacka_auta
        self.typ_auta = typ_auta
        self.pocet_km = pocet_km
        self.obsazenost = True

    def pujc_auto(self):
        if self.obsazenost:
            self.obsazenost = False
            text = "Potvrzuji zapůjčení vozidla."
        else:
            text = "Vozidlo není k dispozici."
        
        return text
    
    def get_info(self):
        return f"Vozidlo má registrační značku {self.registr_znacka}, jeho značka je {self.znacka_auta} a typ {self.typ_auta}."

    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.stav_tachometru = stav_tachometru

        if pocet_dni < 7:
            cena = 400 * pocet_dni
        elif pocet_dni >= 7:
            cena = 300 * pocet_dni

        return f"Cena auta za {pocet_dni} dní je {cena} Kč."




peugeot = Auto("4A2 3020", "Peugeot", "403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda", "Octavia", 41253)

uzivatel = input("Jakou značku auta si přejete půjčit? ")


if uzivatel == "Škoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())
elif uzivatel == "Peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
else:
    print("Vámi zadané auto není v naší nabídce.")

uzivatel = input("Jakou značku auta si přejete půjčit? ")


if uzivatel == "Škoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())
elif uzivatel == "Peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
else:
    print("Vámi zadané auto není v naší nabídce.")

print(skoda.vrat_auto(48500, 8))
