import os


def check_if_file_exists(date, locatia, adj):
    path = "rezultat/"
    file = date + " " + locatia + " " + adj + ".csv"
    if os.path.isfile(path + file):
        return True
    else:
        return False
