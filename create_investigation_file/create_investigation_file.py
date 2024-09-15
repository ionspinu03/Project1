from open_write import open_csv
from create_investigation_file.export_data import export

def transform_data(data):
    valid = []
    c = 0
    for element in data:
        c = c+1
        element["count"] = c
    file_csv = "dictionary/cabinets.csv"
    try:
        cabinet = open_csv(file_csv)
    except:
        print("List of the cabynet type missing. Please check if file exist on 'directory/cabinets.csv'")

    for element in data:
        if element["Transaction Type"] == "DEPOSIT":
            shearch_deposit(element, valid)
        elif element["Transaction Type"] == "WALLET_2_EGM":

            shearch_remote_in(element, valid, data, cabinet)
        elif element["Transaction Type"] == "WITHDRAW_SUM":
            valid = shearch_remote_handpay(element, valid, data)

    file_write_xlsx = export(data, valid)
    return file_write_xlsx

def shearch_deposit(element, valid):
    day = element["Business Day"]
    loc = element["Outlet"]
    ora = element["Time Stamp"][11:]
    event = "Depunere in suma de: " + str(element["Amount"]).replace('.',"").replace(',','.') + " MDL la ora: " + ora
    valid.append({
        "Data":day,
            "Locatia":loc,
            "Seria aparatului":event
            })

    return valid

def shearch_remote_in(element, valid, data, cabinet):
    suma = (element["Amount"])[1:].replace('.',"").replace(',','.')
    day = element["Business Day"]
    loc = element["Outlet"]
    ora = element["Time Stamp"][11:]
    device = element["Device"]
    num = element["count"]
    time = element["Time Stamp"]
    cabin = 0
    for element in cabinet:
        if device == element["Seria"]:
            cabin = element["Cabinet"]
    for element in data:
        if element['count'] == num + 1:
            if element["Transaction Type"] == "EGM_2_WALLET":
                suma_platita = (element["Amount"]).replace('.',"").replace(',','.')
                plata = element["Time Stamp"][11:]
                diferenta  = float(suma_platita) - float(suma)
            elif element["Transaction Type"] != "EGM_2_WALLET":
                suma_platita = 0
                plata = ""
                diferenta  = float(suma_platita) - float(suma)
    
            valid.append({
                "Data": day, 
                "Locatia": loc,
                "Seria aparatului":device, 
                "Cabinet Type": cabin,
                "Ora de intrare":ora, 
                "Time Stamp": time,
                "Suma de intrare":suma, 
                "Suma platita": suma_platita,
                "Diferenta": diferenta,
                "Ora plata": plata
                    })
    return valid

def shearch_remote_handpay(element, valid, data):
    cont = element["count"]
    suma_retrasa = element["Amount"][1:].replace('.',"").replace(',','.')
    for element in data:
        if element["count"] == cont-1:
            if element["Transaction Type"] == "WITHDRAW_TAX":
                suma_retrasa = float(suma_retrasa) + float(element["Amount"][1:].replace('.',"").replace(',','.'))

            day = element["Business Day"]
            loc = element["Outlet"]
            ora = element["Time Stamp"][11:]
            event = "Plata in suma de: " + str(suma_retrasa) + " MDL la ora: " + ora
            valid.append({
                "Data":day,
                "Locatia":loc,
                "Seria aparatului":event
                })
    return valid