import requests, pandas
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(r.content)

platy = pandas.read_csv("platy_2021_02.csv")

# print(platy.head())

# platy.hist(bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000])
# plt.show()

zam_praha = pandas.read_csv("zam_praha.csv")
zam_plzen = pandas.read_csv("zam_plzeň.csv")
zam_liberec = pandas.read_csv("zam_liberec.csv")

zam_praha["mesto"] = "Praha"
zam_plzen["mesto"] = "Plzeň"
zam_liberec["mesto"] = "Liberec"

zamestnanci = pandas.concat([zam_praha, zam_plzen, zam_liberec], ignore_index=True)

zam_platy = pandas.merge(zamestnanci, platy, on=["cislo_zamestnance"], how="outer")


# zam_platy.hist(bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000], by="mesto")
# plt.show()

import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/temperature.csv")
open("temperature.csv", "wb").write(r.content)

teploty = pandas.read_csv("temperature.csv")

teploty_vyber = teploty[teploty["City"].isin(["Helsinki", "Miami Beach", "Tokyo"])]
print(teploty_vyber)

teploty_vyber.plot(kind="box", by="City")
plt.show()