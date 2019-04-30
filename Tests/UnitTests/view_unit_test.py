import unittest
from View.view import View


class ViewTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        # Arrange
        expected_result = '\n'
        # Act
        actual_result = View.newline()
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a Newline')

    def test_02(self):
        # Arrange
        expected_result = '    '
        # Act
        actual_result = View.tab()
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be four spaces')


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # with more details
    # unittest.main()
    # Arrange
    # Act
    # Assert