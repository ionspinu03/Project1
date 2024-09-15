from open_write import open_csv
from multiprocessing_dowload.time_operation import transform_data
from request_report import get_ct_data
# from multiprocessing_dowload.find_element_in_json import find_element_ct


def input_data(date, locatia, adj):
    data, date = transform_data(date)
    adj = insert_adj(adj)
    outlet = atased_outlet(locatia)
    get_ct_data(outlet, data, date, adj)
    # result = ct_execute.text
    
    # find_element_ct(result)


def insert_adj(adj):
    file = "dictionary/ct_lists.csv"
    data = open_csv(file)
    for rows in data:
        if adj in rows["Serial Number"]:
            adj = rows["ID"]
    return adj

def atased_outlet(locatia):
    file = "dictionary/outlet.csv"
    data = open_csv(file)
    for el in data:
        if locatia in el["number"]:
            outlet = el["id_form"]
    return outlet

