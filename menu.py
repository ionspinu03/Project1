from request_report import get_outlet_data
from create_outlet_lists.create_outlet_list import create_outlet_file
from create_ct_lists import create_ct_list
from create_ct_lists.data_operation import save_data
from create_file_uniq_elements.shearch_unic_elements import shearch_unic_elem
from create_file_uniq_elements.create_file_elementele_unice import insert_file
from json_work.json_work import json_work
from multiprocessing_dowload.dowload_uniq_file import multiprocessing_function
from redacted_xlsx_file.style import redacted_xlsx_file

def menu():
    print("1. Adauga cookie")
    print("2. Start ")
    option = input("Enter options: ")

    if option == "3":
            try:
                get_outlet_data()
                create_outlet_file()
                valid = create_ct_list()
                save_data(valid)
            except:
                menu()
            menu()
    elif option == "2":
        file_csv = insert_file()
        file_csv_s = shearch_unic_elem(file_csv)
        file_write_xlsx = multiprocessing_function(file_csv_s)
        path = file_write_xlsx
        redacted_xlsx_file(path)
        menu()

    elif option == "1":
        json_work()
        menu()

if __name__ == "__menu__":
    menu()
