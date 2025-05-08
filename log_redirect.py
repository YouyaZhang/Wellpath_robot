# log_redirect.py

import sys

log_file = open("session_log.txt", "a", encoding="utf-8")
original_stdout = sys.stdout

class Logger:
    def __init__(self, *files):
        self.files = files
    def write(self, message):
        for f in self.files:
            f.write(message)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()

def start_logging():
    sys.stdout = Logger(sys.stdout, log_file)

def stop_logging():
    sys.stdout = original_stdout
    log_file.close()
