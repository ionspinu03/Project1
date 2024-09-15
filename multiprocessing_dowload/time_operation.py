from datetime import datetime
import time

def transform_data(date):
    # date = input("Enter data: ")
    datafrorm = '%d.%m.%Y'
    datato = '%Y-%m-%d'
    datas = datetime.strptime(date, datafrorm).strftime(datato)
    dat = datas+"T12:00:35.063+03:00"
    date_obj = datetime.strptime(dat,"%Y-%m-%dT%H:%M:%S.%f%z").timestamp()
    data = str(date_obj).replace(".", "")
    return data, date