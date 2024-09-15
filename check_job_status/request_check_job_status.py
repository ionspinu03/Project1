from open_write import open_cookie, write_json
import requests
from links import select_link


def check_status_jobs():
    file_cookie = "json_file/cookie.json"
    requests_headres = open_cookie(file_cookie)
    raport = "Job list"
    url = select_link(raport)
    list = requests.post(url, headers=requests_headres)

    file_json = "json_file/job_list.json"
    result = list.text
    write_json(file_json, result)

def check_finished_job(id):
    raport = "Open report by ID"
    url = select_link(raport)
    file_cookie = "json_file/cookie.json"
    requests_headres = open_cookie(file_cookie)
    payload = {"reportId": id, "reportType":""}
    ct_execute = requests.post(url, headers = requests_headres, data = payload)
    return ct_execute

