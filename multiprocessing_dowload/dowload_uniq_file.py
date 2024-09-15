import threading
from queue import Queue
from open_write import open_csv
from multiprocessing_dowload.input_datas import input_data
import os
from create_investigation_file.player import create_file_investigation_and_complete
from tqdm import tqdm

MAX_THREADS = 6


def worker(q, total_jobs, completed_jobs, in_progress, lock, pbar):
    while True:
        item = q.get()
        if item is None:
            break
        with lock:
            in_progress.append(item)

        input_data(item["Business day"], item["Locatia"], item["Aparatul"])

        with lock:
            in_progress.remove(item)
            completed_jobs.append(item)
            pbar.update(1)

        q.task_done()


def multiprocessing_function(file_csv_s):
    file_csv = "rezultat/Investigatii/elementele unice.csv"
    data = open_csv(file_csv)
    download_list = []

    for el in data:
        date = el["Business day"]
        locatia = el["Locatia"]
        adj = el["Aparatul"]
        if not check_if_file_exists(date, locatia, adj):
            download_list.append({
                "Business day": date,
                "Locatia": locatia,
                "Aparatul": adj
            })

    total_jobs = len(download_list)
    completed_jobs = []
    in_progress = []

    print(f"Total de descărcat: {total_jobs}")

    download_queue = Queue()
    for job in download_list:
        download_queue.put(job)

    lock = threading.Lock()
    threads = []

    with tqdm(total=total_jobs, desc="Progres descărcare") as pbar:
        for _ in range(MAX_THREADS):
            t = threading.Thread(target=worker,
                                 args=(download_queue, total_jobs, completed_jobs, in_progress, lock, pbar))
            t.start()
            threads.append(t)

        download_queue.join()

        for _ in range(MAX_THREADS):
            download_queue.put(None)
        for t in threads:
            t.join()

    file_write_xlsx = create_file_investigation_and_complete(file_csv_s)
    return file_write_xlsx


def check_if_file_exists(date, locatia, adj):
    path = "rezultat/"
    file = f"{date} {locatia} {adj}.csv"
    return os.path.isfile(os.path.join(path, file))


if __name__ == "__main__":
    pass
