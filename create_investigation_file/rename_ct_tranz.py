import os
from open_write import open_csv

def rename_ct_tranz():
    file_csv = "rezultat/ct.csv"
    data = open_csv(file_csv)

    for el in data:
        loc = el["outlet"]
        ora = el["time"][1:11]
        adj = el["vlt"]
        print(loc, adj, ora)
        break
    while True:
        try:
            os.rename("rezultat/ct.csv","rezultat/" +  str(ora)+ " " + str(loc) + " " + str(adj)+ ".csv")
        except:
            # print("[-] File already exists or is open")
            break
        continue