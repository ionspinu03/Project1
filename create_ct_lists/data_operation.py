from open_write import open_json, write_csv_file
from create_ct_lists.find_element_in_json import extract_ct_list_element


def search_element():
    file_json = "json_file/ct_list.json"
    ct_listes = open_json(file_json)
    ct_lists = extract_ct_list_element()
    return ct_lists


def save_data(valid):
    directory = "dictionary"
    file_write_csv = "dictionary/ct_lists.csv"
    write_csv_file(file_write_csv, valid, directory)
    print("[+] S-a salvat in: dictionary/ct_lists.csv. \n")