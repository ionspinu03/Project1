from datetime import datetime, timedelta

def find_diference_time(t1, t2):
    dt1 = datetime.strptime(t1," %d.%m.%Y %H:%M:%S").timestamp()
    dt2 = datetime.strptime(t2, " %d.%m.%Y %H:%M:%S").timestamp()

    dt1 = datetime.fromtimestamp(dt1)
    dt2 = datetime.fromtimestamp(dt2)
    delta = dt2 - dt1
    return delta

def check_time(timp1, i):
    dt1 = datetime.strptime(timp1," %d.%m.%Y %H:%M:%S").timestamp()
    dt1 = datetime.fromtimestamp(dt1)
    timp_plus = dt1 + timedelta(seconds=i)
    timp_minus = dt1 - timedelta(seconds=i)

    datato = ' %d.%m.%Y %H:%M:%S'
    timp_plus = datetime.strftime(timp_plus, datato)
    timp_minus = datetime.strftime(timp_minus, datato)
    return timp1, timp_plus, timp_minus