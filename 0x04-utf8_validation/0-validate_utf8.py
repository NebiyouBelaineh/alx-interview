#!/usr/bin/python3
"""Module contains method validUTF8 to verify valid utf-8 data sets"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Verfies if a data set contains valid utf-8 encoding"""
    num_bytes = 0  # number of remaining bytes
    if len(data) == 0:
        return False

    for byte in data:
        if num_bytes == 0:
            # check if the byte is a 2-byte, 3-byte or 4-byte character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):  # Invalid utf-8 character
                return False
        else:
            if (byte >> 6) != 0b10:  # checks continuation byte starts with 10
                return False
            num_bytes -= 1

    return num_bytes == 0
