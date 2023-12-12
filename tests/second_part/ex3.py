from unittest import TestCase
from exercises.second_part import ex3

class TestMain(TestCase):
    def test_main(self):
        statements = [{'height': (175, 185), 'hair': 'black', 'skin': 'white', 'eyes': 'brown', 'clothes': 'black coat'},
                      {'height': (180, 185), 'hair': 'brown', 'skin': 'white', 'eyes': 'green', 'clothes': 'black jacket'},
                      {'height': (170, 185), 'hair': 'black', 'skin': 'white', 'eyes': 'brown', 'clothes': 'black jacket'},
                      ]
        suspects = [{'name': 'Robert', 'height': 180, 'hair': 'black', 'skin': 'white', 'eyes': 'brown', 'clothes': 'black coat'},
                    {'name': 'George', 'height': 189, 'hair': 'brown', 'skin': 'white', 'eyes': 'brown', 'clothes': 'black jacket'},
                    ]
        self.assertEqual(('Robert', 1), ex3.main(statements, suspects))

    def test_eq(self):
        statements = [{'height': (175, 185), 'hair': 'black', 'skin': 'white', 'eyes': 'brown', 'clothes': 'black coat'},
                      {'height': (180, 185), 'hair': 'brown', 'skin': 'white', 'eyes': 'green', 'clothes': 'black jacket'},
                      {'height': (170, 185), 'hair': 'black', 'skin': 'white', 'eyes': 'brown', 'clothes': 'black jacket'},
                      ]
        # same features.
        suspects = [{'name': 'Robert', 'height': 180, 'hair': 'black', 'skin': 'white', 'eyes': 'brown', 'clothes': 'black coat'},
                    {'name': 'George', 'height': 180, 'hair': 'black', 'skin': 'white', 'eyes': 'brown', 'clothes': 'black coat'},
                    ]
        # Should take first
        self.assertEqual(('Robert', 1), ex3.main(statements, suspects))