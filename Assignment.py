import numpy as np

data = np.loadtxt("bank.csv", dtype=np.str, delimiter=";", skiprows=1)


def remove_extra_quotes(para_data):
    # Remove the extra double quotes
    # return null
    for row in para_data:
        for column_idx in range(len(row)):
            row[column_idx] = row[column_idx].replace("\"", "")


remove_extra_quotes(para_data=data)
print(data)
