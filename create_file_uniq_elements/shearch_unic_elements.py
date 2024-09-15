from open_write import open_csv, write_csv_file

def shearch_unic_elem(file_csv):
    unic_elem = []
    valid = []
    data = open_csv(file_csv)
    filter = []

    for element in data:
        if element["Transaction Type"] == "DEPOSIT" or element["Transaction Type"] == "WITHDRAW_TAX" or element["Transaction Type"] == "WITHDRAW_SUM":
            pass
        # elif element["Transaction Type"] == "WITHDRAW_TAX" or element["Transaction Type"] == "WITHDRAW_SUM":
        #     pass
        else:
            location = element["Outlet"]
            day = element["Business Day"]
            adj = element["Device"]
            if element["Transaction Type"] == "WALLET_2_EGM":
                operation = "Start"
            elif element["Transaction Type"] == "EGM_2_WALLET":
                operation = "Plata"
            time = element["Time Stamp"]
            filter.append({"Locatia":location,
                            "Business day": day,
                            "Aparatul": adj,
                            "Timpul": time,
                            "Tipul operatiunii": operation})
    data.clear()
    for elem in filter:
        unic_elem.append({"Locatia":elem["Locatia"],
                            "Business day":elem["Business day"],
                            "Aparatul": elem["Aparatul"]})
    
    
    [valid.append(item) for item in unic_elem if item not in valid]
    directory = "rezultat/Investigatii"
    file_writer_csv = "rezultat/Investigatii/elementele unice.csv"
    write_csv_file(file_writer_csv, valid, directory)
    file_csv_s = file_csv
    return file_csv_s
