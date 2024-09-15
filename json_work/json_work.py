import os
import json

def json_work():
    path = "json_file/"
    file = "cookie.json"
    if os.path.isfile(path + file):
        with open('json_file/cookie.json', "r+") as f:
            file = json.load(f)
            file["Cookie"] ="language=en; region=ro_MD; JSESSIONID=" +  input("Introdu cookie: ")
            f.seek(0)
            json.dump(file, f, indent=4)
            f.truncate()
    else:
        try:
            os.makedirs("json_file", exist_ok = True)
        except OSError as error:
            pass
        with open("json_file/cookie.json", "w") as file:
            file.write("{}")
        with open('json_file/cookie.json', "r+") as f:
            file = json.load(f)
            file["Cookie"] = "language=en; region=ro_MD; JSESSIONID=" + input("Introdu cookie: ")
            f.seek(0)
            json.dump(file, f, indent=4)
            f.truncate()
        print("Datele au fost modificate cu succes\n")
        try:
            os.makedirs("dictionary", exist_ok = True)
        except OSError as error:
            pass


