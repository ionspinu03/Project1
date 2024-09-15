from open_write import open_json
import re


def extract_ct_list_element():
    # data = create_ct_list_file()
    file_json = 'json_file/ct_list.json'
    data = open_json(file_json)
    id = "id:.*"
    outlet = "outlet:.*"
    serial_number = "egmDisplayNumber:.*"

    ct_search = re.compile(id + "|" + outlet + "|" + serial_number)
    all = ct_search.findall(data)
    valid = create_list_csv(all)
    return valid

def create_list_csv(all):
    valid = []
    for row in all:
        if row[0:].startswith("id"):
            id = row.split(":")[1].replace(",","")
            # print(id)
        elif row[0:].startswith("outlet"):
            outlet = row.split(":")[1].replace(",","").replace("'","")
            # print(outlet)
        elif row[0:].startswith("egmDisplayNumber"):
            serial_number = row.split(":")[1].replace(",","").replace('"',"")
            # print(serial_number)
            valid.append({
            "Outlet": outlet,
            "ID": id,
            "Serial Number": serial_number
        })

    return valid

# def create_ct_list_file():
#     data = []
#     file_json = 'json_file/ct_list.json'
#     data = open_json(file_json)
#     return data