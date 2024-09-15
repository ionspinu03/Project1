import re

def extract_outlet_element(data):
    result = []
    id = "id:.*"
    country = "countryCode:.*"
    company = "company:.*"
    number = "oName:.*"
    id_form = "scopeId:.*"

    outlet_search = re.compile(id + "|" + country + "|" + company + "|"  + number + "|" + id_form + "\n" )
    
    all = outlet_search.findall(data)
    for row in all[36:226]:
        result.append(row)
    return result

def extract_outlet_element_2(result):
    valid1 = []

    for el in result:
        el[0] = el[0].split(":")[1].replace("'", "").replace(",", "").replace('"', "").replace(" ", "")
        el[1] = el[1].split(":")[1].replace("'", "").replace(",", "").replace('"', "").replace(" ", "")
        el[2] = el[2].split(":")[1].replace("'", "").replace(",", "").replace('"', "")
        el[3] = el[3].split(":")[1].replace("'", "").replace(",", "").replace('"', "").replace(" ", "")
        el[4] = el[4].split(":")[1].replace("'", "").replace(",", "").replace('"', "").replace(" ", "")
        valid1.append({"id": el[0], "country": el[1], "company": el[2], "number": el[3], "id_form": el[4]})

        lines = valid1.strip().split("\n")

        valid = []

        for line in lines:
            row = line.strip().split(",")
            formatted_row = {}
            for item in row:
                key, value = item.split(": ")
                formatted_row[key] = value.strip('"')
            valid.append(formatted_row)
    return valid