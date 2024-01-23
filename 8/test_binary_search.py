import pytest


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


@pytest.mark.parametrize(
    "arr, target",
    [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)]
)
def test_search_existing_element(arr, target):
    assert binary_search(arr, target) == 4


@pytest.mark.parametrize(
    "arr, target",
    [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)]
)
def test_search_non_existing_element(arr, target):
    assert binary_search(arr, target) == -1


@pytest.mark.parametrize(
    "arr, target",
    [([], 5)]
)
def test_search_empty_array(arr, target):
    assert binary_search(arr, target) == -1
