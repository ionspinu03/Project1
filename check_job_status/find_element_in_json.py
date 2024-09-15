from open_write import open_json
import re


def find_job():
    file_json = "json_file/job_list.json"
    data = open_json(file_json)

    id = "id:.*"
    time = "formattedExecutionTime: .*"
    status = "state: .*"
    check_status = re.compile(id + "|" + time + "|" + status)
    all = check_status.findall(data)
    # print(all)


    job_list =[]
    job_list.clear()
    for rows in all:
        if rows.startswith("id"):
            id = rows.replace('id: "','').replace('",','')
        elif rows.startswith("formattedExecutionTime"):
            data = rows.replace("formattedExecutionTime: '","").replace("',","")
        elif rows.startswith("state"):
            status = rows.replace('state: "','').replace('",','')
            job_list.append({
                "ID": id,
                "Time start execute": data,
                "Status": status
            })
        else:
            pass
    return job_list