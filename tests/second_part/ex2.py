from unittest import TestCase
from exercises.second_part import ex_2

class TestMain(TestCase):
    def test__main(self):
        olympic_games= {'Vancouver(CAN) 2010':{'expenses':'$7B', 'revenue': '$7.5B'},
                        'Sochi(RUS) 2014': {'expenses': '$55B', 'revenue': '$10B'},
                        'Moscow(RUS) 1980': {'expenses': '$6.3B', 'revenue': '$2.8B'},
                        'Sydney(AUS) 2000':{'expenses': '$4.2B', 'revenue': '$1.3B'}}
        expected_result = {
            'RUS': {'info': ['Moscow 1980', 'Sochi 2014'], 'loss': 48.5},
            'CAN': {'info': ['Vancouver 2010'], 'profit': 0.5},
            'AUS': {'info': ['Sydney 2000'], 'loss': 2.9}
        }
        actual_result = ex_2.main(olympic_games)
        self.assertEqual(expected_result, actual_result)