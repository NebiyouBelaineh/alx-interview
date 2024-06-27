#!/usr/bin/python3

validUTF8 = __import__('0-validate_utf8').validUTF8

def run_tests():
    # Test cases
    tests = [
        {
            "description": "Valid UTF-8 sequences",
            "data": [
                [0b11000010, 0b10100010],          # 2-byte character: '¢'
                [0b11100010, 0b10000010, 0b10101100],  # 3-byte character: '€'
                [0b11110000, 0b10010000, 0b10001100, 0b10001100]  # 4-byte character: '𐌌'
            ],
            "expected": True
        },
        {
            "description": "Invalid UTF-8 sequences - invalid continuation byte",
            "data": [
                [0b11000010, 0b00100010],          # 2-byte character with invalid continuation byte
                [0b11100010, 0b00000010, 0b10101100],  # 3-byte character with invalid continuation byte
                [0b11110000, 0b00010000, 0b10001100, 0b10001100]  # 4-byte character with invalid continuation byte
            ],
            "expected": False
        },
        {
            "description": "Invalid UTF-8 sequences - insufficient continuation bytes",
            "data": [
                [0b11000010],                      # 2-byte character but only one byte
                [0b11100010, 0b10000010],          # 3-byte character but only two bytes
                [0b11110000, 0b10010000, 0b10001100]  # 4-byte character but only three bytes
            ],
            "expected": False
        },
        {
            "description": "Empty data sets",
            "data": [
                []
            ],
            "expected": True
        },
        {
            "description": "Data sets containing only ASCII characters",
            "data": [
                [65, 66, 67, 68],  # ASCII characters 'A', 'B', 'C', 'D'
                [32, 33, 34, 35],  # ASCII characters ' ', '!', '"', '#'
            ],
            "expected": True
        },
        {
            "description": "Mix of valid UTF-8 sequences and ASCII characters",
            "data": [
                [65, 0b11000010, 0b10100010, 66],  # 'A', '¢', 'B'
                [32, 0b11100010, 0b10000010, 0b10101100, 33]  # ' ', '€', '!'
            ],
            "expected": True
        },
        {
            "description": "Mix of valid and invalid UTF-8 sequences",
            "data": [
                [65, 0b11000010, 0b00100010, 66],  # 'A', invalid '¢', 'B'
                [32, 0b11100010, 0b00000010, 0b10101100, 33]  # ' ', invalid '€', '!'
            ],
            "expected": False
        },
        {
            "description": "Mix of valid and invalid UTF-8 sequences, ASCII characters, and edge cases",
            "data": [
                [65, 0b11000010, 0b10100010, 66, 0b11110000, 0b00010000, 0b10001100, 0b10001100],  # 'A', '¢', 'B', invalid '𐌌'
                [32, 0b11100010, 0b10000010, 0b10101100, 33, 0b11000010]  # ' ', '€', '!', incomplete 2-byte character
            ],
            "expected": False
        }
    ]

    for test in tests:
        for data_set in test["data"]:
            result = validUTF8(data_set)
            print(f"Test: {test['description']}\nData: {data_set}\nExpected: {test['expected']}, Got: {result}\n")
            assert result == test["expected"], f"Failed test: {test['description']} with data: {data_set}"

run_tests()
