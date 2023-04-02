import requests
import os

def safe_open_w(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'wb')

def download(file_name_or_path, file_url):
    with safe_open_w(file_name_or_path) as download_file:
        download_file.write(requests.get(file_url).content)

def full_update(update_file_url):
    lines = [i.strip() for i in requests.get(update_file_url).content.decode().split("\n")]

    for line in lines:
        if line == "":
            continue
        file, url = line.split("|")
        download(file, url)

def full_update_string(string):
    lines = [i.strip() for i in string.split("\n")]

    for line in lines:
        if line == "":
            continue
        file, url = line.split("|")
        download(file, url)
