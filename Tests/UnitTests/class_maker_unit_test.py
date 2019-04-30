import unittest
from Model.class_maker import ClassMaker


class ClassMakerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        # Arrange
        name = ''
        c_maker = ClassMaker()
        expected_result = ''
        # Act
        actual_result = c_maker.file_name(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_02(self):
        # Arrange
        name = 'AllCapsDays'
        c_maker = ClassMaker()
        expected_result = 'all_caps_days'
        # Act
        actual_result = c_maker.file_name(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_03(self):
        # Arrange
        name = 'AllCapsDays'
        c_maker = ClassMaker()
        expected_result = 'class AllCapsDays:\n'
        # Act
        actual_result = c_maker.class_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_04(self):
        # Arrange
        name = 'newZealand'
        c_maker = ClassMaker()
        expected_result = 'class NewZealand:\n'
        # Act
        actual_result = c_maker.class_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_05(self):
        # Arrange
        name = 'thequickbrownfox'
        c_maker = ClassMaker()
        expected_result = 'class Thequickbrownfox:\n'
        # Act
        actual_result = c_maker.class_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_06(self):
        # Arrange
        name = []
        c_maker = ClassMaker()
        expected_result = ''
        # Act
        actual_result = c_maker.attribute_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_07(self):
        # Arrange
        name = ['']
        c_maker = ClassMaker()
        expected_result = '    def __init__(self):\n        self.\n'
        # Act
        actual_result = c_maker.attribute_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # with more details
    # unittest.main()
    # Arrange
    # Act
    # Assert
