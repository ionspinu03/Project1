
from open_write import open_csv
from create_investigation_file.create_investigation_file import transform_data



def create_file_investigation_and_complete(file_csv_s):
    file_csv = file_csv_s
    print(file_csv)
    data = open_csv(file_csv)
    sorted(data, key=len)
    file_write_xlsx = transform_data(data)
    return file_write_xlsx