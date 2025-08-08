"""
Test functionalities of stats.py
"""
import unittest
import math
import stats as statistics


class StatsTest(unittest.TestCase):
    """Test cases for the stats module."""
    def test_report_min_max_avg(self):
        """Test the calculation of average, max, and min."""
        computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
        epsilon = 0.001
        self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
        self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
        self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

    def test_avg_is_nan_for_empty_input(self):
        """Test the behavior with empty input."""
        computedStats = statistics.calculateStats([])
        self.assertTrue(math.isnan(computedStats["avg"]))
        self.assertTrue(math.isnan(computedStats["max"]))
        self.assertTrue(math.isnan(computedStats["min"]))

    def test_list_is_empty(self):
        """Test the list_is_empty function."""
        self.assertTrue(statistics.list_is_empty([]))
        self.assertFalse(statistics.list_is_empty([1, 2, 3]))

    def test_string_in_list(self):
        """Test the behavior with a list containing a string."""
        computedStats = statistics.calculateStats([1, 2, "three", 4])
        self.assertTrue(math.isnan(computedStats["avg"]))
        self.assertTrue(math.isnan(computedStats["max"]))
        self.assertTrue(math.isnan(computedStats["min"]))

    def test_space_in_list(self):
        """Test the behavior with a list containing a space."""
        computedStats = statistics.calculateStats([1, 2, " ", 4])
        self.assertTrue(math.isnan(computedStats["avg"]))
        self.assertTrue(math.isnan(computedStats["max"]))
        self.assertTrue(math.isnan(computedStats["min"]))


if __name__ == "__main__":
    unittest.main()
