import requests
from open_write import open_cookie, write_json
from links import select_link
import requests
from check_job_status.check_status import check_jobs
from find_elements import find_element_ct


def vlt_lists():
    file_cookie = "json_file/cookie.json"
    requests_headres = open_cookie(file_cookie)
    payload = {"scopes": "company,21901",
    "_activeOnly": "",
    "activeOnly": "on",
    "_eodPendingOnly": "",
    "pendingMoreThanNHours": "1",
    "egmDisplayNumber": ""}
    raport = "vlt"
    url = select_link(raport)
    ct_list = requests.post(url, headers = requests_headres, data = payload)
    file_json = "json_file/ct_list.json"
    result = ct_list.text
    write_json(file_json, result)
    return

def get_outlet_data():
    file_cookie = "json_file/cookie.json"
    raport = "outlet"
    requests_headres = open_cookie(file_cookie)
    url = select_link(raport)

    outlet = requests.get(url, headers = requests_headres)


    file_name = "json_file/outlets.json"
    result = outlet.text
    write_json(file_name, result)

    return

def get_ct_data(outlet, data, date, adj):
    file_cookie = "json_file/cookie.json"
    requests_headres = open_cookie(file_cookie)
    raport = "ct"
    # outlet, data, date, adj = insert_data.input_data()
    url = select_link(raport)

    payload = {"scopes": "outlet,21901," + outlet, "date": date, "filterDevice": adj, "preselectedDeviceId": "", "dateGMT": data}
    result = requests.post(url, headers =  requests_headres, data = payload)
    if result.status_code == 200:
        result = result.text
        find_element_ct(result)
        
        # return ct_execute
    elif result.status_code == 504:
        results =  check_jobs()
        for i in range(0,len(results)):
            result = results[i]
            find_element_ct(result)

    return
    