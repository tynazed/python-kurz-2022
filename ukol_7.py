import re

with open("posta.html", encoding="utf-8") as vstup:
    stranka_posta = vstup.read()

stranka_posta = stranka_posta.replace("\n", " ")
# print(stranka_posta)

reg_vyraz = re.compile("\s+")

stranka_posta = re.sub(reg_vyraz, " ", stranka_posta)
# print(stranka_posta)

reg_vyraz_mesto = re.compile("\d{3}\s\d{2}\s[a-žA-Ž\s*a-žA-Ž]*\d*")

psc_mesta = reg_vyraz_mesto.findall(stranka_posta)
# print(psc_mesta)

for psc in psc_mesta:
    print(psc)