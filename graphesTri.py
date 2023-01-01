#!/usr/bin/python3
from matplotlib import pyplot as plt
insertion = [0.77, 3.15, 12.43, 28.33, 79.66, 157.49, 323.74]
selection = [0.85, 3.10, 12.62, 27.85, 77.36, 151.78, 311.41]
bubble = [3.17, 11.51, 47.81, 106.71, 294.39, 579.67, 1311.64]
merge = [1.05, 4.24, 16.34, 36.82, 102.33, 202.13, 491.23]
quick = [0.01, 0.02, 0.04, 0.06, 0.09, 0.15, 0.22]
pile = [17.34, 67.73, 266.44, 596.16, 1568.43, 3113.21, 7430.30]

x = [5000, 10000, 20000, 30000, 50000, 70000, 100000]
for i in range(len(x)):
    plt.plot(x[i], insertion[i], 'gx')      #insertion : green
    plt.plot(x[i], selection[i], 'rx')      #selection : red
    plt.plot(x[i], bubble[i], 'yx')         #bubble : yellow
    plt.plot(x[i], merge[i], 'gx')          #merge : gray
    plt.plot(x[i], quick[i], 'bx')          #quick : blue
    plt.plot(x[i], pile[i], 'cx')           #pile : cyan
plt.title("Graphe de comparaison de l'efficacité des algos de tris")
plt.show()
