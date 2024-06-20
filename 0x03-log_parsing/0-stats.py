#!/usr/bin/python3
"""Modue to count status codes and file size every 10 line of input"""
import sys

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


def print_stats(file_size: int, status_codes: dict) -> None:
    """Prints stats counted"""
    print(f'File size: {file_size}')
    for key, value in status_code.items():
        if value:
            print(f'{key}: {value}')


def count_stats() -> None:
    """Counts the stats and lines from stdin"""
    try:
        for line in sys.stdin:
            global file_size
            global line_number
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
    except Exception:
        pass
    finally:
        print_stats(file_size, status_code)
        sys.exit()


count_stats()
