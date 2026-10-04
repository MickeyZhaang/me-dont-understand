"""
heapq module from scratch
"""


def heapify(x: list):
    """
    turns list into a min-heap
    """
    new_x = []

    for e in x:
        heappush(new_x, e)
    x[:] = new_x


def _parent_index(index: int):
    """
    finds the parent of the current value at index and returns the parent's index
    """
    if index == 0:
        return None
    return (index - 1) // 2


def _left_child_index(x: list, index: int):
    """
    finds the left child, if it exists, and returns the child's index
    """
    idx = (index * 2) + 1
    return idx if idx < len(x) else None


def _right_child_index(x: list, index: int):
    """
    finds the right child, if it exists, and returns the child's index
    """
    idx = (index * 2) + 2
    return idx if idx < len(x) else None


def _sift_up(x: list, index: int):
    while index > 0:
        parent_idx = _parent_index(index)

        if x[parent_idx] <= x[index]:
            break
        x[parent_idx], x[index] = (x[index], x[parent_idx])

        index = parent_idx


def _sift_down(x: list, index: int):
    while True:
        left, right = _left_child_index(x, index), _right_child_index(x, index)

        if not left:
            break

        min_idx = left

        if right is not None and x[right] < x[left]:
            min_idx = right

        x[min_idx], x[index] = x[index], x[min_idx]
        index = min_idx


def heappush(x: list, v: int):
    """
    pushes onto our input list x
    """
    x.append(v)
    _sift_up(x, len(x) - 1)


def heappop(x: list):
    """
    pops off our input list x
    """
    if not x:
        return None
    popped = x[0]
    last = x.pop()

    if x:
        x[0] = last
        _sift_down(x, 0)

    return popped
