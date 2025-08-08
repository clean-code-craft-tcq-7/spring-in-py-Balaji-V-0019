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


if __name__ == "__main__":
    unittest.main()
