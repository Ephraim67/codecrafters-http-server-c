import requests
from threading import Thread
import time
from termcolor import colored
from utilities import log_result, handle_headers, handle_retry

class request_performer(Thread):
    def __init__(self, word, url, hidecode, output, proxy, headers, delay, retry):
        super().__init__()
        self.word = word.strip()
        self.url = url.replace("FUZZ", self.word)
        self.hidecode = hidecode
        self.output = output
        self.proxy = proxy
        self.headers = handle_headers(headers)
        self.delay = delay
        self.retry = retry
    
    def run(self):
        global active_threads
        try:
            response = handle_retry(self.url, self.proxy, self.headers, self.retry)
            if response and str(response.status_code) not in self.hidecodes:
                color = 'green' if response.status_code < 300 else 'red' if response.status_code < 500 else 'yellow'
                result = f"{response.status_code}\t{len(response.text)}\t{self.url}"
                print(colored(result, color))

                if self.output:
                    log_result(result, self.output)
            time.sleep(self.delay)
            active_threads[0] -= 1
        except Exception as e:
            print(f"Error: {e}")

def launch_threads(words, url, max_threads, hidecodes, output, proxy, headers, delay, retry):
    global active_threads
    active_threads = [0]
    threads = []

    while words:
        if active_threads[0] < max_threads:
            words= words.pop(0)
            active_threads[0] += 1
            thread = request_performer(words, url, hidecodes, output, proxy, headers, delay, retry)
            thread.start()
            threads.append()

    for thread in threads:
        thread.join()