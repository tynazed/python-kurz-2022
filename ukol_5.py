class Polozka():
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr
    
    def get_info(self):
        return f"Název: {self.nazev}, žánr: {self.zanr}"

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka

    def get_info(self):
        return super().get_info() + f", délka filmu: {self.delka} minut"
    
    def get_celkova_delka(self):
        delka = self.delka
        return delka


class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody

    def get_info(self):
        return super().get_info() + f", počet epizod: {self.pocet_epizod}"
    
    def get_celkova_delka(self):
        delka = self.pocet_epizod * self.delka_epizody
        return delka

class Uzivatel():
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0
    
    def pripocti_zhlednuti(self, delka):
        self.delka_sledovani += delka


film = Film("Forrest Gump", "Drama/Komedie/Romantický", 142)
print(film.get_info())
serial = Serial("Sherlock", "Krimi/Mysteriózní/Drama", 12, 90)
print(serial.get_info())

uzivatel = Uzivatel("Jan Horký")


uzivatel.pripocti_zhlednuti(film.get_celkova_delka())
print(uzivatel.delka_sledovani)

uzivatel.pripocti_zhlednuti(serial.get_celkova_delka())
print(uzivatel.delka_sledovani)

