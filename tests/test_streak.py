import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test with a list containing only non-positive numbers."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_all_positive_numbers():
    """Test with a list of all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak_at_beginning():
    """Test a single streak at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 0, -1, -2]) == 3

def test_single_streak_at_end():
    """Test a single streak at the end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4

def test_multiple_streaks_longest_is_last():
    """Test multiple streaks where the longest one is at the end."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3]) == 3

def test_multiple_streaks_longest_is_first():
    """Test multiple streaks where the longest one is at the beginning."""
    assert longest_positive_streak([1, 2, 3, 4, -5, 1, 2]) == 4

def test_streaks_separated_by_negatives():
    """Test streaks separated by negative numbers."""
    assert longest_positive_streak([1, 2, -3, 4, 5, 6, -7, 8]) == 3

def test_streaks_separated_by_zeros():
    """Test streaks separated by zeros."""
    assert longest_positive_streak([1, 0, 2, 3, 0, 4, 5, 6, 7]) == 4

def test_list_with_single_zero():
    """Test with a single zero, which should result in a streak of 0."""
    assert longest_positive_streak([0]) == 0

def test_list_with_single_positive_number():
    """Test with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_complex_case():
    """A more complex test case with mixed numbers."""
    assert longest_positive_streak([1, 2, 0, 4, 5, -1, 7, 8, 9, 0, 1]) == 3