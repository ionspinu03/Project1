import time
from check_job_status.request_check_job_status import check_status_jobs
from check_job_status.find_element_in_json import find_job
from check_job_status.request_check_job_status import check_finished_job

def check_jobs():
    check_status_jobs()
    job_list = find_job()
    result = check_status(job_list)

    results = []
    for el in result:
        id_search = el["ID"]
        ct_execute = check_if_job_finished(id_search)
        if ct_execute is not None and hasattr(ct_execute, 'text'):
            results.append(ct_execute.text)
        else:
            results.append(f"Job {id_search} did not finish properly or returned None")
    return results

def check_status(job_list):
    result = [element for element in job_list if element["Status"] == "IN_PROGRESS"]
    return result

def check_if_job_finished(id_search):
    for _ in range(100):
        check_status_jobs()
        job_list = find_job()
        for element in job_list:
            if id_search == element["ID"]:
                if element["Status"] == "IN_PROGRESS":
                    time.sleep(20)
                elif element["Status"] == "FINISHED":
                    ct_execute = check_finished_job(id_search)
                    return ct_execute
    return None

if __name__ == "__main__":
    pass
