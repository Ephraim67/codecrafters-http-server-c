import random
import requests

def banner():
    print("*********************************************************************************************")
    print("[                      ]")
    print(" \                     / Starting ")

def load_worldlist(filename):
    try:
        with open(filename, 'r')as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Wordlist {filename} not found.")
        return []
    
def handle_headers(headers):
    return {k: v for h in headers for k, v in [h.split(": ")]} if headers else {}

def log_result(result, output_file):
    with open(output_file, 'a') as f:
        f.write(result + "\n")

def handle_retry(url, proxy, headers, retry_count):
    for _ in range(retry_count):
        try:
            return requests.get(url, headers=headers, proxies={"http":proxy, "https":proxy} if proxy else None)
        except requests.RequestException:
            continue
    return None