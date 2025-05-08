from turtledemo.penrose import start

import matplotlib.pyplot as plt

"""
years = [2006 + x for x in range(8)]
weights = [20, 40, 60, 70, 170, 50, 30, 18]
plt.plot(years, weights, "r--", lw=2)

plt.show()
"""


linguagens = ["Java", "PHP", "JS", "React", "C"]
votos = [16, 9, 8, 3, 5]
explodes = [0, 0.02, 0, 0, 0]
plt.pie(votos, labels=linguagens, explode = explodes, autopct="%.2f%%")

plt.show()

"""
anos = [2012, 2013, 2014, 2015,
        2016, 2017, 2018, 2019]

dpmn = [21, 23, 19, 11,
        13, 12, 12, 17]

etiquetasDeDpmn = list(range(5, 25, 2))

plt.plot(anos, dpmn, "r--")
plt.title("Felicidade média por ano, de 0 a 25", fontsize=20)
plt.xlabel("Ano")
plt.ylabel("Felicidade registrada")
plt.yticks(etiquetasDeDpmn, [f"{x}ml DM" for x in etiquetasDeDpmn])
plt.show()
"""



""" Vídeo utilizado de suporte: Matplotlib Full Python Course - Data Science Fundamentals
https: // youtu.be / OZOOLe2imFo?si = b_c7T0z3339RSHSj   """
