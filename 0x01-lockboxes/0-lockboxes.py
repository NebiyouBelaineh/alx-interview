#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked or not

    Args:
        boxes (list[list]): List of lists containing box with keys inside
    Returns:
        boolean: true | false
    """
    keys = set()  # Tracks keys using a set
    keys.update(boxes[0])

    opened_boxes = set()  # Tracks boxes opened using a set
    opened_boxes.add(0)  # Box 0 always unlocked

    while len(keys) > 0:  # While there are keys to try
        box = keys.pop()

        if box not in opened_boxes and box < len(boxes):
            opened_boxes.add(box)
            keys.update(boxes[box])
    # print(f"opened_boxes: {opened_boxes}")
    if len(opened_boxes) == len(boxes):
        return True
    return False
