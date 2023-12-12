from exercises.first_part import ex3
from unittest import TestCase


class GetBest__TestCase(TestCase):
    def test__min_points(self):
        rest_scores = {'A': {'min_points': -1, '++': 2},
                       'B': {'min_points': 1, '++': 3},
                       'C': {'min_points': 2, '++': 1}}
        actual = ex3.get_best(rest_scores)
        expected = 'C'
        self.assertEqual(actual, expected)

    def test__pluses(self):
        rest_scores = {'A': {'min_points': 1, '++': 2},
                       'B': {'min_points': 1, '++': 3},
                       'C': {'min_points': 1, '++': 1}}
        actual = ex3.get_best(rest_scores)
        expected = 'B'
        self.assertEqual(actual, expected)

    def test__alph(self):
        rest_scores = {'A': {'min_points': 1, '++': 1},
                       'B': {'min_points': 1, '++': 1},
                       'C': {'min_points': 1, '++': 1}}
        actual = ex3.get_best(rest_scores)
        expected = 'A'
        self.assertEqual(actual, expected)

