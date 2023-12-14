import unittest
from unittest import TestCase
import pandas as pd
from exercises.first_part import ex6


class TestMain(TestCase):
    def test__main(self):
        grades = pd.DataFrame({'2017-02-05': {'Hermione': 5, 'Ron': 2},
                               '2017-02-12': {'Hermione': float('nan'), 'Ron': float('nan')},
                               '2017-02-19': {'Hermione': 7.0, 'Ron': float('nan')},
                               '2017-02-26': {'Hermione': float('nan'), 'Ron': 4.0}})

        plan = pd.DataFrame({'activity': {0: 'Test', 1: 'Test', 2: 'Seminar', 3: 'Seminar'},
                             'date': {0: '2017-02-05', 1: '2017-02-12', 2: '2017-02-19', 3: '2017-02-26'}})

        excuses = pd.DataFrame({'name': {0: 'Hermione', 1: 'Hermione', 2: 'Ron', 3: 'Harry'},
                                'date': {0: '2017-02-10 2017-02-11', 1: '2017-02-12 2017-02-12', 2: '2017-02-19 2017-02-19', 3: '2017-02-19 2017-02-19'},
                                'reason': {0: 'valid', 1: 'valid', 2: 'invalid', 3: 'invalid'}})

        expected_result = pd.Series({'Hermione': 4, 'Ron': 2})
        actual_result = ex6.main(grades, excuses, plan)
        for index in expected_result.index:
            expected_value = expected_result[index]
            actual_value = actual_result[index]
            self.assertEqual(actual_value, expected_value)


# class TestIsValidExcuse(unittest.TestCase):
#     def test__first(self):
#         excuses = pd.DataFrame({'name': ['Ron'],
#                                 'date': ['2010-01-10 2010-01-20'],
#                                 'reason': ['valid']})
#
#         name = 'Ron'
#         date = '2010-01-10'
#         self.assertEqual(True, ex6.is_valid_excuse(excuses, date, name))