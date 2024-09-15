from create_file_uniq_elements.shearch_unic_elements import shearch_unic_elem

def insert_file():
    print("Trage fisierul cu denumirea PlayerTransaction ->>")
    file_csv = input().replace('& ', '').replace("'","").replace('"','')

    return file_csv