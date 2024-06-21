#!/usr/bin/python3
"""Modue to count status codes and file size every 10 line of input"""
import sys
import re

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

            pattern = re.compile(
                r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
                r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] '
                r'"GET /projects/260 HTTP/1.1" '
                r'(\d{3}) '
                r'(\d+)$'
                )
            if not pattern.match(line):
                continue
            line_number += 1
            input = line.strip()
            splited_input = input.split()
            if len(splited_input) < 5:
                continue
            f_size, s_code = splited_input[-1], splited_input[-2]
            file_size += int(f_size)
            valid_stats_code = ((s_code in status_code.keys()
                                or str(s_code) in status_code.keys())
                                and s_code.isdigit())
            if valid_stats_code:
                status_code[splited_input[-2]] += 1
            else:
                continue
            if line_number % 10 == 0:
                print_stats(file_size, status_code)
    except Exception as e:
        print(e)
    finally:
        print_stats(file_size, status_code)
        sys.exit()


count_stats()
