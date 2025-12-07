from pandas.core.dtypes.astype import astype_array_safe

import app

def test_generate_random_list_length_and_range():
    numbers = app.generate_random_list()
    assert len(numbers) == 9
    assert all(1 <= n <= 50 for n in numbers)

def test_generate_random_list_with_custom_params():
    numbers = app.generate_random_list(n=5, low=3, high=10)
    assert len(numbers) == 5
    assert all(3 <= n <= 10 for n in numbers)

def sort_buble_sort_basic_case():
    data = [5,3,1,2,4]
    sorted_data = app.bubble_sort(data)
    assert sorted_data == [1,2,3,4,5]

def test_bubble_sort_does_not_mutate_input():
    data = [3,2,1]
    original_copy = data[:]
    sorted_data = app.bubble_sort(data)
    # original list unchanged
    assert data == original_copy
    # result is sorted
    assert sorted_data == [1,2,3]

def test_bubble_sort_already_sorted():
    data = [1, 2, 3, 4]
    sorted_data = app.bubble_sort(data)
    assert sorted_data == [1, 2, 3, 4]


def test_bubble_sort_with_duplicates():
    data = [3, 1, 2, 3, 1]
    sorted_data = app.bubble_sort(data)
    assert sorted_data == [1, 1, 2, 3, 3]