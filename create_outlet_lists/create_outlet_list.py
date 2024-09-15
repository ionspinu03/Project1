from open_write import open_json, open_file, csv_reader, write_csv_file
from create_outlet_lists.data_operation import extract_outlet_element, extract_outlet_element_2

def create_outlet_file():
    data = []
    valid = []
    file_json = 'json_file/outlets.json'
    data = open_json(file_json)
    result = extract_outlet_element(data)
    directory = "dictionary"
    file_name = "dictionary/outlet.csv"
    file = open_file(file_name, directory)
    for row in result:
        file.write(row)
    file.close()
    result.clear()
    file_csv = "dictionary/outlet.csv"    
    result = csv_reader(file_csv, directory)
    valid = extract_outlet_element_2(result)
    directory = "dictionary"
    file_write_csv = "dictionary/outlet.csv"
    write_csv_file (file_write_csv, valid, directory)