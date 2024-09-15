import requests
import os
import re
import csv
from open_write import open_cookie, write_json, open_file, write_csv_file, open_json, open_csv


def main():
    id = input("Introdu id-ul: ")
    file_cookie = "json_file/cookie.json"
    requests_headers = open_cookie(file_cookie)
    url = "https://wrmi.s219.vnet.services/ctTransactionsReport/viewReport"
    payload = {"reportId": id, "reportType": ""}
    ct_execute = requests.post(url, headers=requests_headers, data=payload)
    file_json = "json_file/ct.json"
    write_json(file_json, ct_execute.text)

    process_ct_elements()


def process_ct_elements():
    all_elements = extract_ct_elements()
    all_elements[7:].sort()
    write_raw_csv(all_elements[7:])
    valid_data = create_valid_csv_data()
    write_valid_csv(valid_data)
    rename_ct_file()


def extract_ct_elements():
    data = load_json_data('json_file/ct.json')
    patterns = ["id:.*", "vlt:.*", "action:.*", "description:.*",
                "outletDisplayNumberFormatted:.*", "trnTimeFormatted:.*", "amountFormatted:.*"]
    ct_search = re.compile("|".join(patterns) + "\n")
    return ct_search.findall(data)


def load_json_data(file_path):
    return open_json(file_path)


def write_raw_csv(elements):
    with open("rezultat/ct.csv", 'w') as file:
        file.writelines(elements)


def create_valid_csv_data():
    result = []
    with open("rezultat/ct.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            result.append(row)

    valid_data = []
    for el in result:
        valid_data.append({
            "id": clean_value(el[0], "id"),
            "outlet": clean_value(el[4], "outlet"),
            "vlt": clean_value(el[1], "vlt"),
            "action": clean_value(el[2], "action"),
            "time": clean_value(el[5], "trnTimeFormatted"),
            "amount": clean_value(el[6], "amountFormatted") + "." + el[7].replace("'", ""),
            "description": el[3].replace("'", "").replace(",", "").replace('"', "").replace("description:", "")
        })
    return valid_data


def clean_value(value, prefix):
    return value.split(":")[1].replace("'", "").replace(",", "").replace('"', "").replace(" ", "")


def write_valid_csv(valid_data):
    write_csv_file("rezultat/ct.csv", valid_data, "rezultat")


def rename_ct_file():
    data = open_csv("rezultat/ct.csv")
    if data:
        loc = data[0]["outlet"]
        ora = data[0]["time"][1:11]
        adj = data[0]["vlt"]
        os.rename("rezultat/ct.csv", f"rezultat/{ora} {loc} {adj}.csv")


if __name__ == "__main__":
    main()
