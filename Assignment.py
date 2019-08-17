import numpy as np

data = np.loadtxt("bank.csv", dtype=np.str, delimiter=";", skiprows=1)

print(data)
