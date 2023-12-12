from unittest import TestCase
from exercises.first_part import ex2


class Ex2Test(TestCase):
    def test__main(self):
        sales = {"2022.02": {"products": ["apple", "melon"],
                             "quantity_sold": ["j4", "25"], "price": ["j0", "j4"], "cost": ["j60", "300"]},
                 "2022.04": {"products": ["peach", "melon"],
                             "quantity_sold": ["22", "20"], "price": ["5", "j4"], "cost": ["j20", "400"]},
                 "2022.10": {"products": ["peach", "kiwi", "apple"],
                             "quantity_sold": ["25", "72", "2j"], "price": ["5", "6", "j0"],
                             "cost": ["j20", "450", "240"]},
                 "2021.10": {"products": ["kiwi", "pear", "melon", "apple"],
                             "quantity_sold": ["j5", "44", "23", "8j"], "price": ["5", "3", "j3", "j0"],
                             "cost": ["95", "j00", "300", "800"]},
                 "2022.01": {"products": ["kiwi", "melon", "apple"],
                             "quantity_sold": ["85", "55", "j00"], "price": ["7", "jj", "j0"],
                             "cost": ["600", "540", "800"]},
                 "2022.03": {"products": ["pear", "apple", "peach"],
                             "quantity_sold": ["54", "66", "40"], "price": ["5", "jj", "4"],
                             "cost": ["300", "700", "180"]}}

        revenue_expected = {'kiwi': {'revenue': 1102, 'profit': -43, 'sales_months': ['2021.10', '2022.01', '2022.10']},
           'pear': {'revenue': 402, 'profit': 2, 'sales_months': ['2021.10', '2022.03']},
           'melon': {'revenue': 1534, 'profit': -6, 'sales_months': ['2021.10', '2022.01', '2022.02', '2022.04']},
           'apple': {'revenue': 2886, 'profit': 186, 'sales_months': ['2021.10', '2022.01', '2022.02', '2022.03', '2022.10']},
           'peach': {'revenue': 395, 'profit': -25, 'sales_months': ['2022.03', '2022.04', '2022.10']}}
        revenue_actual = ex2.main(sales)

        for fruit in revenue_expected.keys():
            expected_stat = revenue_expected[fruit]
            actual_stat = revenue_actual[fruit]
            self.assertEqual(expected_stat, actual_stat)