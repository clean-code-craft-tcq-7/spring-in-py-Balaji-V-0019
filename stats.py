"""
stats.py - Module for calculating statistics
like average, max, and min from a list of numbers.
"""
import math


def list_is_empty(numbers):
    """Check if the input list is empty."""
    return len(numbers) == 0


def calculateStats(numbers):
    """Calculate average, max, and min of a list of numbers."""
    computedStats = {
        "avg": math.nan,
        "max": math.nan,
        "min": math.nan
    }
    if list_is_empty(numbers):
        return computedStats

    computedStats["avg"] = math.fsum(numbers) / len(numbers)
    computedStats["max"] = max(numbers)
    computedStats["min"] = min(numbers)
    return computedStats
