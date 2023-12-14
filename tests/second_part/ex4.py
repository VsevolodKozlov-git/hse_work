import unittest
from exercises.second_part import ex4


class TestMain(unittest.TestCase):
    def test_main(self):
        string = '"May the Force be with you" - "Star Wars" 1977'
        expected = {'3 letter words': ['May', 'the', 'you'],
                     '5 letter words': ['Force'],
                     '2 letter words': ['be'],
                     '4 letter words': ['with', 'Star', 'Wars']}
        actual = ex4.main(string)
        self.assertEqual(expected, actual)

    def test_underscore(self):
        string = 'hello_world'
        expected = {'5 letter words': ['hello', 'world']}
        actual = ex4.main(string)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
