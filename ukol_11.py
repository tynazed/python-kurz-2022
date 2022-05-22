import pandas, requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_praha.csv")
open("zam_praha.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_plzeň.csv")
open("zam_plzeň.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_liberec.csv")
open("zam_liberec.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(r.content)

zam_praha = pandas.read_csv("zam_praha.csv")
zam_plzen = pandas.read_csv("zam_plzeň.csv")
zam_liberec = pandas.read_csv("zam_liberec.csv")
platy_2021 = pandas.read_csv("platy_2021_02.csv")

zam_praha["mesto"] = "Praha"
zam_plzen["mesto"] = "Plzeň"
zam_liberec["mesto"] = "Liberec"

zamestnanci = pandas.concat([zam_praha, zam_plzen, zam_liberec], ignore_index=True)

print(zamestnanci)

zamestnanci_platy = pandas.merge(zamestnanci, platy_2021, on=["cislo_zamestnance"], how="outer")
print(zamestnanci_platy)

print(zamestnanci_platy.groupby("mesto")["plat"].mean())

#zaměstnanci, kteří ve firmě už nepracují
byvali_zamestnanci = zamestnanci_platy[zamestnanci_platy["plat"].isnull()]
print(byvali_zamestnanci)

byvali_zamestnanci.to_csv("byvali_zam.csv", index=False, sep=";", columns=["jmeno", "prijimeni", "telefonni_cislo", "cislo_zamestnance", "mesto"])

# Projekty
r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/vykazy.csv")
open("vykazy.csv", "wb").write(r.content)

vykazy = pandas.read_csv("vykazy.csv")
print(vykazy.head())

#počet vykázaných hodin na jednotlivých projektech
print(vykazy.groupby("project")["hours"].sum())

zamestnanci_vykazy = pandas.merge(zamestnanci_platy, vykazy, left_on="cislo_zamestnance", right_on="emloyee_id")
print(zamestnanci_vykazy)

# počet vykázaných hodin zaměstnanci jednotlivých kanceláří na jednotlivých projektech
print(zamestnanci_vykazy.groupby(by=["project", "mesto"])["hours"].sum())

