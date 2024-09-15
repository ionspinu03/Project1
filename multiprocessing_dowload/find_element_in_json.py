from open_write import write_csv_file
import re
# import pandas as pd

def find_element_ct(result):
    all = extract_ct_element(result)
    data = []
    for row in all[7:]:
        if row.startswith('id: "'):
            id = row.replace('id: "','').replace('",','')
        elif row.startswith("vlt: '"):
            vlt = row.replace("vlt: '","").replace("',","")
        elif row.startswith('action: "'):
            action = row.replace('action: "',"").replace('",','')
        elif row.startswith('description: "'):
            description = row.replace('description: "',"").replace('",','')
        elif row.startswith("outletDisplayNumberFormatted: '"):
            outlet = row.replace("outletDisplayNumberFormatted: '","").replace("',",'')
        elif row.startswith("trnTimeFormatted: '"):
            time = " " + row.replace("trnTimeFormatted: '","").replace("',",'')
        elif row.startswith("amountFormatted: '"):
            ammount = row.replace("amountFormatted: '","").replace("',",'').replace("\n","")
            try:
                ammount = ammount.replace(".","")
            finally:
                pass
            try:
                ammount = ammount.replace(",",".")
            finally:
                pass
            data.append({
                "id": id,
                "outlet": outlet,
                "vlt": vlt,
                "action": action,
                "time": time,
                "amount": ammount,
                "description": description
            })

    for el in data:
        loc = el["outlet"]
        ora = el["time"][1:11]
        adj = el["vlt"]   
        break


    file_write_csv = "rezultat/" + str(ora) + " " + str(loc) + " " + str(adj)+ ".csv"
    directory = "rezultat/"
    write_csv_file(file_write_csv, data, directory)
    
def extract_ct_element(result):
    id = "id:.*"
    vlt = "vlt:.*"
    action = "action:.*"
    description = "description:.*"
    outlet = "outletDisplayNumberFormatted:.*"
    time = "trnTimeFormatted:.*"
    amount = "amountFormatted:.*"
    
    ct_search = re.compile(id + "|" + vlt + "|" + action + "|"  + description + "|" + outlet + "|" + time  + "|" + amount + "\n" )
    all = ct_search.findall(result)
    return all