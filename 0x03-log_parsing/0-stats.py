#!/usr/bin/python3
"""Modue to count status codes and file size every 10 line of input"""
import sys
import signal

file_size = 0
line_number = 0
status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats(file_size, status_codes):
    """Prints stats counted"""
    print(f'File size: {file_size}')
    for key, value in status_code.items():
        if value:
            print(f'{key}: {value}')


def count_stats():
    """Counts the stats and lines from stdin"""
    for line in sys.stdin:
        global line_number
        global file_size
        global status_code

        line_number += 1
        input = line.strip()
        splited_input = input.split()
        f_size, s_code = splited_input[-1], splited_input[-2]
        file_size += int(f_size)
        valid_stats_code = (s_code in status_code.keys()
                            or str(s_code) in status_code.keys())
        if valid_stats_code:
            status_code[splited_input[-2]] += 1
        else:
            continue
        if line_number % 10 == 0:
            print_stats(file_size, status_code)


def signal_handler(sig, frame):
    """Handle ctrl + c signal"""
    global file_size
    global status_code
    print_stats(file_size, status_code)


signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    count_stats()
