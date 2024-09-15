import json
import os
import csv
import pandas as pd

def open_cookie(file_cookie):
    with open(file_cookie, "r") as f:
        requests_headres = json.load(f)
    return requests_headres

def write_json(file_json, result):
    with open(file_json, "w", encoding="utf-8") as data_file:
        data_file.write(result)

def open_json(file_json):
    data =[]
    with open(file_json, "r") as json_file:
        data = json_file.read()
    return data

def open_file(file_name, directory):
    path = os.curdir + "/" + directory
    try:
        os.makedirs(path, exist_ok = True)
    except OSError as error:
        pass
    file = open(file_name, "w")
    return file

def csv_reader(file_csv, directory):
    path = os.curdir + "/" + directory
    try:
        os.makedirs(path, exist_ok = True)
    except OSError as error:
        pass
    result = []
    with open(file_csv, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            result.append(row)
    return result

def write_csv_file(file_write_csv, valid, directory):
    path = os.curdir + "/" + directory
    try:
        os.makedirs(path, exist_ok = True)
    except OSError as error:
        pass
    pd.DataFrame(valid).to_csv(file_write_csv, index=False, sep = ";")

def open_csv(file_csv):
    try:
        data = []
        with open(file_csv) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter = ";")
            for rows in csv_reader:
                data.append(rows)
        return data
    except:
        print("[-] File ct.csv not exits")

def write_to_xlsx_file(file_write_xlsx, valid, directory):
    path = os.curdir + "/" + directory
    try:
        os.makedirs(path, exist_ok = True)
    except OSError as error:
        pass
    pd.DataFrame(valid).to_excel(file_write_xlsx, index=False)