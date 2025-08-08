"""
stats.py - Module for calculating statistics
like average, max, and min from a list of numbers.
"""
import math


def list_is_empty(numbers):
    """Check if the input list is empty."""
    return len(numbers) == 0


def is_valid_list(numbers):
    """Check if the input list is valid (non-empty and contains numbers)."""
    if list_is_empty(numbers):
        return False
    if not all(isinstance(x, (int, float)) for x in numbers):
        return False
    return True


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if is_valid_list(numbers):
        return math.fsum(numbers) / len(numbers)
    return math.nan


def calculate_max(numbers):
    """Calculate the maximum of a list of numbers."""
    if is_valid_list(numbers):
        return max(numbers)
    return math.nan


def calculate_min(numbers):
    """Calculate the minimum of a list of numbers."""
    if is_valid_list(numbers):
        return min(numbers)
    return math.nan


def calculateStats(numbers):
    """Calculate average, max, and min of a list of numbers."""
    computedStats = {
        "avg": calculate_average(numbers),
        "max": calculate_max(numbers),
        "min": calculate_min(numbers)
    }
    return computedStats
