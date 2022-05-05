import pandas

adopce_zvirat = pandas.read_csv("adopce-zvirat.csv", sep=";")

adopce_zvirat.info()

print(adopce_zvirat.columns)

print(adopce_zvirat.iloc[34, 1:3])

adopce_zvirat_index = pandas.read_csv("adopce-zvirat.csv", sep=";", index_col=1)

print(adopce_zvirat_index)

print(adopce_zvirat_index.index.is_unique)

adopce_zvirat_index = adopce_zvirat_index.sort_index()

print(adopce_zvirat_index)

print(adopce_zvirat_index.loc["Outloň váhavý"])

print(adopce_zvirat_index.loc["Želva Smithova":"Želva žlutočelá"])