import pandas, pytemperature

teploty = pandas.read_csv("temperature.csv")

print("Prvních pár záznamů tabulky")
print(teploty.head())

print("Teplota vyšší než 80")
print(teploty[teploty["AvgTemperature"] > 80])

print("Teplota vyšší než 60 v Evropě")
print(teploty[(teploty["AvgTemperature"] > 60) & (teploty["Region"] == "Europe")])

print("Teplota vyšší než 80 nebo nižší než -20")
print(teploty[(teploty["AvgTemperature"] > 80) | (teploty["AvgTemperature"] < -20)])

##Bonus 1
print("nový sloupec")
teploty["AvgTemperatureCelsia"] = pytemperature.f2c(teploty["AvgTemperature"])
print(teploty.head())

print("teplota vyšší než 30")
print(teploty[teploty["AvgTemperatureCelsia"] > 30])

print("teplota vyšší než 15 v Evropě")
print(teploty[(teploty["AvgTemperatureCelsia"] > 15) & (teploty["Region"] == "Europe")])

print("teplota vyšší než 30 nebo nižší než -10")
print(teploty[(teploty["AvgTemperatureCelsia"] > 30) | (teploty["AvgTemperatureCelsia"] < -10)])
## hodnoty -99F jsou chybné, asi chyba měření nebo není žádná hodnota

##Bonus 2
print("teplota 13. listopadu")
print(teploty[teploty["Day"] == 13])

print("teplota 13. listopadu v USA")
print(teploty[(teploty["Day"] == 13) & (teploty["Country"] == "US")])
teploty_USA = teploty[(teploty["Day"] == 13) & (teploty["Country"] == "US")]

print("teplota 13. listopadu v USA ve Washingtonu a Philadelphii")
print(teploty_USA[teploty_USA["City"].isin(["Washington", "Philadelphia"])])

