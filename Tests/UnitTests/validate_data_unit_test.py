import unittest
from validate_data import ValidateData


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        # Arrange
        data = ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n', '@enduml']
        validate = ValidateData(data)
        expected_result = True
        # Act
        actual_result = validate.check_start_uml()
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be True')

    def test_02(self):
        # Arrange
        data = ['class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n', '@enduml']
        validate = ValidateData(data)
        expected_result = False
        # Act
        actual_result = validate.check_start_uml()
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be False')

    def test_03(self):
        # Arrange
        data = ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n', '@enduml']
        validate = ValidateData(data)
        expected_result = True
        # Act
        actual_result = validate.check_end_uml()
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be False')

    def test_04(self):
        # Arrange
        data = ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n']
        validate = ValidateData(data)
        expected_result = False
        # Act
        actual_result = validate.check_end_uml()
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be False')

    def test_05(self):
        # Arrange
        data = ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n',
                'class GamePlayer{\\n', 'myPosition', '}\\n', '@enduml']
        validate = ValidateData(data)
        expected_result = True
        # Act
        actual_result = validate.check_class_count()
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be False')

    def test_05(self):
        # Arrange
        data = ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n', '@enduml']
        validate = ValidateData(data)
        expected_result = True
        # Act
        actual_result = validate.check_class_count()
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be False')

    def test_06(self):
        # Arrange
        data = ['@startuml\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n']
        validate = ValidateData(data)
        expected_result = False
        # Act
        actual_result = validate.check_class_count()
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be False')


if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()
    # Arrange
    # Act
    # Assert
